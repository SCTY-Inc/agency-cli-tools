"""
Graph retrieval tools service.
Encapsulates graph search, node reading, edge queries, and other tools for use by the Report Agent.

Core retrieval tools (optimized):
1. InsightForge (deep insight retrieval) - The most powerful hybrid retrieval, automatically generates sub-queries and retrieves across multiple dimensions
2. PanoramaSearch (broad search) - Get the full picture, including expired content
3. QuickSearch (simple search) - Fast retrieval
"""

import time
import json
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

from .graph_db import GraphDatabase
from .graph_storage import GraphStorage

from ..utils.logger import get_logger
from ..utils.llm_client import LLMClient

logger = get_logger('mirofish.graph_tools')


@dataclass
class SearchResult:
    """Search result"""
    facts: List[str]
    edges: List[Dict[str, Any]]
    nodes: List[Dict[str, Any]]
    query: str
    total_count: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "facts": self.facts,
            "edges": self.edges,
            "nodes": self.nodes,
            "query": self.query,
            "total_count": self.total_count
        }

    def to_text(self) -> str:
        """Convert to text format for LLM comprehension"""
        text_parts = [f"Search query: {self.query}", f"Found {self.total_count} relevant pieces of information"]

        if self.facts:
            text_parts.append("\n### Relevant Facts:")
            for i, fact in enumerate(self.facts, 1):
                text_parts.append(f"{i}. {fact}")

        return "\n".join(text_parts)


@dataclass
class NodeInfo:
    """Node information"""
    uuid: str
    name: str
    labels: List[str]
    summary: str
    attributes: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "labels": self.labels,
            "summary": self.summary,
            "attributes": self.attributes
        }

    def to_text(self) -> str:
        """Convert to text format"""
        entity_type = next((l for l in self.labels if l not in ["Entity", "Node"]), "Unknown type")
        return f"Entity: {self.name} (Type: {entity_type})\nSummary: {self.summary}"


@dataclass
class EdgeInfo:
    """Edge information"""
    uuid: str
    name: str
    fact: str
    source_node_uuid: str
    target_node_uuid: str
    source_node_name: Optional[str] = None
    target_node_name: Optional[str] = None
    # Temporal information
    created_at: Optional[str] = None
    valid_at: Optional[str] = None
    invalid_at: Optional[str] = None
    expired_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "fact": self.fact,
            "source_node_uuid": self.source_node_uuid,
            "target_node_uuid": self.target_node_uuid,
            "source_node_name": self.source_node_name,
            "target_node_name": self.target_node_name,
            "created_at": self.created_at,
            "valid_at": self.valid_at,
            "invalid_at": self.invalid_at,
            "expired_at": self.expired_at
        }

    def to_text(self, include_temporal: bool = False) -> str:
        """Convert to text format"""
        source = self.source_node_name or self.source_node_uuid[:8]
        target = self.target_node_name or self.target_node_uuid[:8]
        base_text = f"Relationship: {source} --[{self.name}]--> {target}\nFact: {self.fact}"

        if include_temporal:
            valid_at = self.valid_at or "Unknown"
            invalid_at = self.invalid_at or "Present"
            base_text += f"\nValidity: {valid_at} - {invalid_at}"
            if self.expired_at:
                base_text += f" (Expired: {self.expired_at})"

        return base_text

    @property
    def is_expired(self) -> bool:
        """Whether the edge has expired"""
        return self.expired_at is not None

    @property
    def is_invalid(self) -> bool:
        """Whether the edge has been invalidated"""
        return self.invalid_at is not None


@dataclass
class InsightForgeResult:
    """
    Deep insight retrieval result (InsightForge)
    Contains retrieval results for multiple sub-queries and comprehensive analysis
    """
    query: str
    simulation_requirement: str
    sub_queries: List[str]

    # Retrieval results by dimension
    semantic_facts: List[str] = field(default_factory=list)  # Semantic search results
    entity_insights: List[Dict[str, Any]] = field(default_factory=list)  # Entity insights
    relationship_chains: List[str] = field(default_factory=list)  # Relationship chains

    # Statistics
    total_facts: int = 0
    total_entities: int = 0
    total_relationships: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "simulation_requirement": self.simulation_requirement,
            "sub_queries": self.sub_queries,
            "semantic_facts": self.semantic_facts,
            "entity_insights": self.entity_insights,
            "relationship_chains": self.relationship_chains,
            "total_facts": self.total_facts,
            "total_entities": self.total_entities,
            "total_relationships": self.total_relationships
        }

    def to_text(self) -> str:
        """Convert to detailed text format for LLM comprehension"""
        text_parts = [
            f"## Future Prediction Deep Analysis",
            f"Analysis question: {self.query}",
            f"Prediction scenario: {self.simulation_requirement}",
            f"\n### Prediction Data Statistics",
            f"- Relevant prediction facts: {self.total_facts} items",
            f"- Entities involved: {self.total_entities} items",
            f"- Relationship chains: {self.total_relationships} items"
        ]

        # Sub-queries
        if self.sub_queries:
            text_parts.append(f"\n### Analyzed Sub-queries")
            for i, sq in enumerate(self.sub_queries, 1):
                text_parts.append(f"{i}. {sq}")

        # Semantic search results
        if self.semantic_facts:
            text_parts.append(f"\n### [Key Facts] (Please cite these original texts in the report)")
            for i, fact in enumerate(self.semantic_facts, 1):
                text_parts.append(f"{i}. \"{fact}\"")

        # Entity insights
        if self.entity_insights:
            text_parts.append(f"\n### [Core Entities]")
            for entity in self.entity_insights:
                text_parts.append(f"- **{entity.get('name', 'Unknown')}** ({entity.get('type', 'Entity')})")
                if entity.get('summary'):
                    text_parts.append(f"  Summary: \"{entity.get('summary')}\"")
                if entity.get('related_facts'):
                    text_parts.append(f"  Related facts: {len(entity.get('related_facts', []))} items")

        # Relationship chains
        if self.relationship_chains:
            text_parts.append(f"\n### [Relationship Chains]")
            for chain in self.relationship_chains:
                text_parts.append(f"- {chain}")

        return "\n".join(text_parts)


@dataclass
class PanoramaResult:
    """
    Broad search result (Panorama)
    Contains all relevant information, including expired content
    """
    query: str

    # All nodes
    all_nodes: List[NodeInfo] = field(default_factory=list)
    # All edges (including expired ones)
    all_edges: List[EdgeInfo] = field(default_factory=list)
    # Currently valid facts
    active_facts: List[str] = field(default_factory=list)
    # Expired/invalidated facts (historical records)
    historical_facts: List[str] = field(default_factory=list)

    # Statistics
    total_nodes: int = 0
    total_edges: int = 0
    active_count: int = 0
    historical_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "all_nodes": [n.to_dict() for n in self.all_nodes],
            "all_edges": [e.to_dict() for e in self.all_edges],
            "active_facts": self.active_facts,
            "historical_facts": self.historical_facts,
            "total_nodes": self.total_nodes,
            "total_edges": self.total_edges,
            "active_count": self.active_count,
            "historical_count": self.historical_count
        }

    def to_text(self) -> str:
        """Convert to text format (full version, no truncation)"""
        text_parts = [
            f"## Broad Search Results (Future Panoramic View)",
            f"Query: {self.query}",
            f"\n### Statistics",
            f"- Total nodes: {self.total_nodes}",
            f"- Total edges: {self.total_edges}",
            f"- Currently valid facts: {self.active_count} items",
            f"- Historical/expired facts: {self.historical_count} items"
        ]

        # Currently valid facts (full output, no truncation)
        if self.active_facts:
            text_parts.append(f"\n### [Currently Valid Facts] (Simulation result originals)")
            for i, fact in enumerate(self.active_facts, 1):
                text_parts.append(f"{i}. \"{fact}\"")

        # Historical/expired facts (full output, no truncation)
        if self.historical_facts:
            text_parts.append(f"\n### [Historical/Expired Facts] (Evolution process records)")
            for i, fact in enumerate(self.historical_facts, 1):
                text_parts.append(f"{i}. \"{fact}\"")

        # Key entities (full output, no truncation)
        if self.all_nodes:
            text_parts.append(f"\n### [Entities Involved]")
            for node in self.all_nodes:
                entity_type = next((l for l in node.labels if l not in ["Entity", "Node"]), "Entity")
                text_parts.append(f"- **{node.name}** ({entity_type})")

        return "\n".join(text_parts)


@dataclass
class AgentInterview:
    """Single agent's interview result"""
    agent_name: str
    agent_role: str  # Role type (e.g., student, teacher, media, etc.)
    agent_bio: str  # Biography
    question: str  # Interview question
    response: str  # Interview response
    key_quotes: List[str] = field(default_factory=list)  # Key quotes

    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_name": self.agent_name,
            "agent_role": self.agent_role,
            "agent_bio": self.agent_bio,
            "question": self.question,
            "response": self.response,
            "key_quotes": self.key_quotes
        }

    def to_text(self) -> str:
        text = f"**{self.agent_name}** ({self.agent_role})\n"
        # Display the full agent_bio without truncation
        text += f"_Bio: {self.agent_bio}_\n\n"
        text += f"**Q:** {self.question}\n\n"
        text += f"**A:** {self.response}\n"
        if self.key_quotes:
            text += "\n**Key Quotes:**\n"
            for quote in self.key_quotes:
                # Clean up various quotation marks
                clean_quote = quote.replace('\u201c', '').replace('\u201d', '').replace('"', '')
                clean_quote = clean_quote.replace('\u300c', '').replace('\u300d', '')
                clean_quote = clean_quote.strip()
                # Remove leading punctuation
                while clean_quote and clean_quote[0] in '，,；;：:、。！？\n\r\t ':
                    clean_quote = clean_quote[1:]
                # Filter out junk content containing question numbers (Question 1-9)
                skip = False
                for d in '123456789':
                    if f'\u95ee\u9898{d}' in clean_quote:
                        skip = True
                        break
                if skip:
                    continue
                # Truncate overly long content (truncate at period, not hard cut)
                if len(clean_quote) > 150:
                    dot_pos = clean_quote.find('\u3002', 80)
                    if dot_pos > 0:
                        clean_quote = clean_quote[:dot_pos + 1]
                    else:
                        clean_quote = clean_quote[:147] + "..."
                if clean_quote and len(clean_quote) >= 10:
                    text += f'> "{clean_quote}"\n'
        return text


@dataclass
class InterviewResult:
    """
    Interview result (Interview)
    Contains interview responses from multiple simulated agents
    """
    interview_topic: str  # Interview topic
    interview_questions: List[str]  # Interview question list

    # Agents selected for interview
    selected_agents: List[Dict[str, Any]] = field(default_factory=list)
    # Interview responses from each agent
    interviews: List[AgentInterview] = field(default_factory=list)

    # Reasoning for agent selection
    selection_reasoning: str = ""
    # Consolidated interview summary
    summary: str = ""

    # Statistics
    total_agents: int = 0
    interviewed_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "interview_topic": self.interview_topic,
            "interview_questions": self.interview_questions,
            "selected_agents": self.selected_agents,
            "interviews": [i.to_dict() for i in self.interviews],
            "selection_reasoning": self.selection_reasoning,
            "summary": self.summary,
            "total_agents": self.total_agents,
            "interviewed_count": self.interviewed_count
        }

    def to_text(self) -> str:
        """Convert to detailed text format for LLM comprehension and report citation"""
        text_parts = [
            "## In-Depth Interview Report",
            f"**Interview Topic:** {self.interview_topic}",
            f"**Interviewees:** {self.interviewed_count} / {self.total_agents} simulated agents",
            "\n### Interviewee Selection Reasoning",
            self.selection_reasoning or "(Automatically selected)",
            "\n---",
            "\n### Interview Transcripts",
        ]

        if self.interviews:
            for i, interview in enumerate(self.interviews, 1):
                text_parts.append(f"\n#### Interview #{i}: {interview.agent_name}")
                text_parts.append(interview.to_text())
                text_parts.append("\n---")
        else:
            text_parts.append("(No interview records)\n\n---")

        text_parts.append("\n### Interview Summary and Key Insights")
        text_parts.append(self.summary or "(No summary)")

        return "\n".join(text_parts)


class GraphToolsService:
    """
    Graph retrieval tools service.

    [Core Retrieval Tools - Optimized]
    1. insight_forge - Deep insight retrieval (most powerful, auto-generates sub-queries, multi-dimensional retrieval)
    2. panorama_search - Broad search (get the full picture, including expired content)
    3. quick_search - Simple search (fast retrieval)
    4. interview_agents - In-depth interview (interview simulated agents, obtain multi-perspective viewpoints)

    [Basic Tools]
    - search_graph - Graph semantic search
    - get_all_nodes - Get all nodes in the graph
    - get_all_edges - Get all edges in the graph (with temporal information)
    - get_node_detail - Get detailed node information
    - get_node_edges - Get edges related to a node
    - get_entities_by_type - Get entities by type
    - get_entity_summary - Get relationship summary for an entity
    """

    # Retry configuration
    MAX_RETRIES = 3
    RETRY_DELAY = 2.0

    def __init__(
        self,
        llm_client: Optional[LLMClient] = None,
        storage: Optional[GraphStorage] = None,
    ):
        self.db = GraphDatabase()
        self.storage = storage
        # LLM client used for InsightForge sub-query generation
        self._llm_client = llm_client
        logger.info("GraphToolsService initialized successfully (using local GraphDatabase)")

    @property
    def llm(self) -> LLMClient:
        """Lazy initialization of the LLM client"""
        if self._llm_client is None:
            self._llm_client = LLMClient()
        return self._llm_client

    def _node_value(self, node: Any, attr: str, key: str, default: Any = "") -> Any:
        if hasattr(node, attr):
            return getattr(node, attr)
        return node.get(key, default)

    def _node_labels(self, node: Any) -> List[str]:
        if hasattr(node, "labels"):
            return node.labels or []
        label = node.get("label", "Entity")
        return ["Entity"] if label == "Entity" else ["Entity", label]

    def _edge_value(self, edge: Any, attr: str, key: str, default: Any = "") -> Any:
        if hasattr(edge, attr):
            return getattr(edge, attr)
        return edge.get(key, default)

    def _call_with_retry(self, func, operation_name: str, max_retries: int = None):
        """API call with retry mechanism"""
        max_retries = max_retries or self.MAX_RETRIES
        last_exception = None
        delay = self.RETRY_DELAY

        for attempt in range(max_retries):
            try:
                return func()
            except Exception as e:
                last_exception = e
                if attempt < max_retries - 1:
                    logger.warning(
                        f"{operation_name} attempt {attempt + 1} failed: {str(e)[:100]}, "
                        f"retrying in {delay:.1f}s..."
                    )
                    time.sleep(delay)
                    delay *= 2
                else:
                    logger.error(f"{operation_name} still failed after {max_retries} attempts: {str(e)}")

        raise last_exception

    def search_graph(
        self,
        graph_id: str,
        query: str,
        limit: int = 10,
        scope: str = "edges"
    ) -> SearchResult:
        """
        Graph search

        Uses local keyword matching to search for relevant information in the graph.

        Args:
            graph_id: Graph ID (Standalone Graph)
            query: Search query
            limit: Number of results to return
            scope: Search scope, "edges" or "nodes"

        Returns:
            SearchResult: Search results
        """
        logger.info(f"Graph search: graph_id={graph_id}, query={query[:50]}...")

        try:
            if self.storage is not None:
                return self._local_search(graph_id, query, limit, scope)

            search_results = self.db.search(graph_id=graph_id, query=query, limit=limit, scope=scope)

            facts = []
            edges = []
            nodes = []

            for item in search_results:
                if item.get("type") == "edge":
                    fact = item.get("fact", "")
                    if fact:
                        facts.append(fact)
                    edges.append({
                        "uuid": item.get("uuid", ""),
                        "name": item.get("name", ""),
                        "fact": fact,
                        "source_node_uuid": item.get("source_node_uuid", ""),
                        "target_node_uuid": item.get("target_node_uuid", ""),
                    })
                elif item.get("type") == "node":
                    nodes.append({
                        "uuid": item.get("uuid", ""),
                        "name": item.get("name", ""),
                        "labels": item.get("labels", []),
                        "summary": item.get("summary", ""),
                    })
                    # Node summaries also count as facts
                    summary = item.get("summary", "")
                    if summary:
                        facts.append(f"[{item.get('name', '')}]: {summary}")

            logger.info(f"Search completed: found {len(facts)} relevant facts")

            return SearchResult(
                facts=facts,
                edges=edges,
                nodes=nodes,
                query=query,
                total_count=len(facts)
            )

        except Exception as e:
            logger.warning(f"Graph search failed, falling back to local search: {str(e)}")
            # Fallback: use local keyword matching search
            return self._local_search(graph_id, query, limit, scope)

    def _local_search(
        self,
        graph_id: str,
        query: str,
        limit: int = 10,
        scope: str = "edges"
    ) -> SearchResult:
        """
        Local keyword matching search (fallback)

        Fetches all edges/nodes and performs local keyword matching.

        Args:
            graph_id: Graph ID
            query: Search query
            limit: Number of results to return
            scope: Search scope

        Returns:
            SearchResult: Search results
        """
        logger.info(f"Using local search: query={query[:30]}...")

        facts = []
        edges_result = []
        nodes_result = []

        # Extract query keywords (simple tokenization)
        query_lower = query.lower()
        keywords = [w.strip() for w in query_lower.replace(',', ' ').replace('，', ' ').split() if len(w.strip()) > 1]

        def match_score(text: str) -> int:
            """Calculate match score between text and query"""
            if not text:
                return 0
            text_lower = text.lower()
            # Exact query match
            if query_lower in text_lower:
                return 100
            # Keyword matching
            score = 0
            for keyword in keywords:
                if keyword in text_lower:
                    score += 10
            return score

        try:
            if scope in ["edges", "both"]:
                # Get all edges and match
                all_edges = self.get_all_edges(graph_id)
                scored_edges = []
                for edge in all_edges:
                    score = match_score(edge.fact) + match_score(edge.name)
                    if score > 0:
                        scored_edges.append((score, edge))

                # Sort by score
                scored_edges.sort(key=lambda x: x[0], reverse=True)

                for score, edge in scored_edges[:limit]:
                    if edge.fact:
                        facts.append(edge.fact)
                    edges_result.append({
                        "uuid": edge.uuid,
                        "name": edge.name,
                        "fact": edge.fact,
                        "source_node_uuid": edge.source_node_uuid,
                        "target_node_uuid": edge.target_node_uuid,
                    })

            if scope in ["nodes", "both"]:
                # Get all nodes and match
                all_nodes = self.get_all_nodes(graph_id)
                scored_nodes = []
                for node in all_nodes:
                    score = match_score(node.name) + match_score(node.summary)
                    if score > 0:
                        scored_nodes.append((score, node))

                scored_nodes.sort(key=lambda x: x[0], reverse=True)

                for score, node in scored_nodes[:limit]:
                    nodes_result.append({
                        "uuid": node.uuid,
                        "name": node.name,
                        "labels": node.labels,
                        "summary": node.summary,
                    })
                    if node.summary:
                        facts.append(f"[{node.name}]: {node.summary}")

            logger.info(f"Local search completed: found {len(facts)} relevant facts")

        except Exception as e:
            logger.error(f"Local search failed: {str(e)}")

        return SearchResult(
            facts=facts,
            edges=edges_result,
            nodes=nodes_result,
            query=query,
            total_count=len(facts)
        )

    def get_all_nodes(self, graph_id: str) -> List[NodeInfo]:
        """
        Get all nodes in the graph

        Args:
            graph_id: Graph ID

        Returns:
            List of nodes
        """
        logger.info(f"Fetching all nodes for graph {graph_id}...")

        if self.storage is not None:
            nodes = self.storage.list_nodes()
        else:
            nodes = self.db.get_all_nodes(graph_id)

        result = []
        for node in nodes:
            result.append(NodeInfo(
                uuid=self._node_value(node, "uuid_", "id") or "",
                name=self._node_value(node, "name", "name") or "",
                labels=self._node_labels(node),
                summary=self._node_value(node, "summary", "summary") or "",
                attributes=self._node_value(node, "attributes", "attributes", {}) or {}
            ))

        logger.info(f"Fetched {len(result)} nodes")
        return result

    def get_all_edges(self, graph_id: str, include_temporal: bool = True) -> List[EdgeInfo]:
        """
        Get all edges in the graph (including temporal information)

        Args:
            graph_id: Graph ID
            include_temporal: Whether to include temporal information (default True)

        Returns:
            List of edges (including created_at, valid_at, invalid_at, expired_at)
        """
        logger.info(f"Fetching all edges for graph {graph_id}...")

        if self.storage is not None:
            edges = self.storage.get_edges()
        else:
            edges = self.db.get_all_edges(graph_id)

        result = []
        for edge in edges:
            edge_info = EdgeInfo(
                uuid=self._edge_value(edge, "uuid_", "id") or "",
                name=self._edge_value(edge, "name", "relation") or "",
                fact=self._edge_value(edge, "fact", "fact") or "",
                source_node_uuid=self._edge_value(edge, "source_node_uuid", "source_id") or "",
                target_node_uuid=self._edge_value(edge, "target_node_uuid", "target_id") or ""
            )

            # Add temporal information
            if include_temporal:
                edge_info.created_at = self._edge_value(edge, "created_at", "created_at", None)
                edge_info.valid_at = self._edge_value(edge, "valid_at", "valid_at", None)
                edge_info.invalid_at = self._edge_value(edge, "invalid_at", "invalid_at", None)
                edge_info.expired_at = self._edge_value(edge, "expired_at", "expired_at", None)

            result.append(edge_info)

        logger.info(f"Fetched {len(result)} edges")
        return result

    def get_node_detail(self, graph_id: str, node_uuid: str) -> Optional[NodeInfo]:
        """
        Get detailed information for a single node

        Args:
            graph_id: Graph ID
            node_uuid: Node UUID

        Returns:
            Node information or None
        """
        logger.info(f"Fetching node detail: {node_uuid[:8]}...")

        try:
            node = self.storage.get_node(node_uuid) if self.storage is not None else self.db.get_node(graph_id, node_uuid)

            if not node:
                return None

            return NodeInfo(
                uuid=self._node_value(node, "uuid_", "id") or "",
                name=self._node_value(node, "name", "name") or "",
                labels=self._node_labels(node),
                summary=self._node_value(node, "summary", "summary") or "",
                attributes=self._node_value(node, "attributes", "attributes", {}) or {}
            )
        except Exception as e:
            logger.error(f"Failed to get node detail: {str(e)}")
            return None

    def get_node_edges(self, graph_id: str, node_uuid: str) -> List[EdgeInfo]:
        """
        Get all edges related to a node

        Args:
            graph_id: Graph ID
            node_uuid: Node UUID

        Returns:
            List of edges
        """
        logger.info(f"Fetching edges for node {node_uuid[:8]}...")

        try:
            if self.storage is not None:
                edges = self.storage.get_edges(source_id=node_uuid) + self.storage.get_edges(target_id=node_uuid)
            else:
                edges = self.db.get_node_edges(graph_id, node_uuid)

            result = []
            for edge in edges:
                result.append(EdgeInfo(
                    uuid=self._edge_value(edge, "uuid_", "id") or "",
                    name=self._edge_value(edge, "name", "relation") or "",
                    fact=self._edge_value(edge, "fact", "fact") or "",
                    source_node_uuid=self._edge_value(edge, "source_node_uuid", "source_id") or "",
                    target_node_uuid=self._edge_value(edge, "target_node_uuid", "target_id") or "",
                    created_at=self._edge_value(edge, "created_at", "created_at", None),
                    valid_at=self._edge_value(edge, "valid_at", "valid_at", None),
                    invalid_at=self._edge_value(edge, "invalid_at", "invalid_at", None),
                    expired_at=self._edge_value(edge, "expired_at", "expired_at", None)
                ))

            logger.info(f"Found {len(result)} edges related to the node")
            return result

        except Exception as e:
            logger.warning(f"Failed to get node edges: {str(e)}")
            return []

    def get_entities_by_type(
        self,
        graph_id: str,
        entity_type: str
    ) -> List[NodeInfo]:
        """
        Get entities by type

        Args:
            graph_id: Graph ID
            entity_type: Entity type (e.g., Student, PublicFigure, etc.)

        Returns:
            List of entities matching the type
        """
        logger.info(f"Fetching entities of type {entity_type}...")

        all_nodes = self.get_all_nodes(graph_id)

        filtered = []
        for node in all_nodes:
            # Check if labels contain the specified type
            if entity_type in node.labels:
                filtered.append(node)

        logger.info(f"Found {len(filtered)} entities of type {entity_type}")
        return filtered

    def get_entity_summary(
        self,
        graph_id: str,
        entity_name: str
    ) -> Dict[str, Any]:
        """
        Get relationship summary for a specified entity

        Searches for all information related to the entity and generates a summary.

        Args:
            graph_id: Graph ID
            entity_name: Entity name

        Returns:
            Entity summary information
        """
        logger.info(f"Fetching relationship summary for entity {entity_name}...")

        # First search for information related to the entity
        search_result = self.search_graph(
            graph_id=graph_id,
            query=entity_name,
            limit=20
        )

        # Try to find the entity among all nodes
        all_nodes = self.get_all_nodes(graph_id)
        entity_node = None
        for node in all_nodes:
            if node.name.lower() == entity_name.lower():
                entity_node = node
                break

        related_edges = []
        if entity_node:
            # Pass graph_id parameter
            related_edges = self.get_node_edges(graph_id, entity_node.uuid)

        return {
            "entity_name": entity_name,
            "entity_info": entity_node.to_dict() if entity_node else None,
            "related_facts": search_result.facts,
            "related_edges": [e.to_dict() for e in related_edges],
            "total_relations": len(related_edges)
        }

    def get_graph_statistics(self, graph_id: str) -> Dict[str, Any]:
        """
        Get graph statistics

        Args:
            graph_id: Graph ID

        Returns:
            Statistics information
        """
        logger.info(f"Fetching statistics for graph {graph_id}...")

        nodes = self.get_all_nodes(graph_id)
        edges = self.get_all_edges(graph_id)

        # Count entity type distribution
        entity_types = {}
        for node in nodes:
            for label in node.labels:
                if label not in ["Entity", "Node"]:
                    entity_types[label] = entity_types.get(label, 0) + 1

        # Count relationship type distribution
        relation_types = {}
        for edge in edges:
            relation_types[edge.name] = relation_types.get(edge.name, 0) + 1

        return {
            "graph_id": graph_id,
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "entity_types": entity_types,
            "relation_types": relation_types
        }

    def get_simulation_context(
        self,
        graph_id: str,
        simulation_requirement: str,
        limit: int = 30
    ) -> Dict[str, Any]:
        """
        Get simulation-related context information

        Performs a comprehensive search for all information related to the simulation requirement.

        Args:
            graph_id: Graph ID
            simulation_requirement: Simulation requirement description
            limit: Quantity limit per information category

        Returns:
            Simulation context information
        """
        logger.info(f"Fetching simulation context: {simulation_requirement[:50]}...")

        # Search for information related to the simulation requirement
        search_result = self.search_graph(
            graph_id=graph_id,
            query=simulation_requirement,
            limit=limit
        )

        # Get graph statistics
        stats = self.get_graph_statistics(graph_id)

        # Get all entity nodes
        all_nodes = self.get_all_nodes(graph_id)

        # Filter entities with actual types (not pure Entity nodes)
        entities = []
        for node in all_nodes:
            custom_labels = [l for l in node.labels if l not in ["Entity", "Node"]]
            if custom_labels:
                entities.append({
                    "name": node.name,
                    "type": custom_labels[0],
                    "summary": node.summary
                })

        return {
            "simulation_requirement": simulation_requirement,
            "related_facts": search_result.facts,
            "graph_statistics": stats,
            "entities": entities[:limit],  # Limit quantity
            "total_entities": len(entities)
        }

    # ========== Core Retrieval Tools (Optimized) ==========

    def insight_forge(
        self,
        graph_id: str,
        query: str,
        simulation_requirement: str,
        report_context: str = "",
        max_sub_queries: int = 5
    ) -> InsightForgeResult:
        """
        [InsightForge - Deep Insight Retrieval]

        The most powerful hybrid retrieval function that automatically decomposes queries and retrieves across multiple dimensions:
        1. Uses LLM to decompose the question into multiple sub-queries
        2. Performs semantic search for each sub-query
        3. Extracts related entities and retrieves their detailed information
        4. Traces relationship chains
        5. Integrates all results to generate deep insights

        Args:
            graph_id: Graph ID
            query: User question
            simulation_requirement: Simulation requirement description
            report_context: Report context (optional, for more precise sub-query generation)
            max_sub_queries: Maximum number of sub-queries

        Returns:
            InsightForgeResult: Deep insight retrieval result
        """
        logger.info(f"InsightForge deep insight retrieval: {query[:50]}...")

        result = InsightForgeResult(
            query=query,
            simulation_requirement=simulation_requirement,
            sub_queries=[]
        )

        # Step 1: Use LLM to generate sub-queries
        sub_queries = self._generate_sub_queries(
            query=query,
            simulation_requirement=simulation_requirement,
            report_context=report_context,
            max_queries=max_sub_queries
        )
        result.sub_queries = sub_queries
        logger.info(f"Generated {len(sub_queries)} sub-queries")

        # Step 2: Perform semantic search for each sub-query
        all_facts = []
        all_edges = []
        seen_facts = set()

        for sub_query in sub_queries:
            search_result = self.search_graph(
                graph_id=graph_id,
                query=sub_query,
                limit=15,
                scope="edges"
            )

            for fact in search_result.facts:
                if fact not in seen_facts:
                    all_facts.append(fact)
                    seen_facts.add(fact)

            all_edges.extend(search_result.edges)

        # Also search with the original query
        main_search = self.search_graph(
            graph_id=graph_id,
            query=query,
            limit=20,
            scope="edges"
        )
        for fact in main_search.facts:
            if fact not in seen_facts:
                all_facts.append(fact)
                seen_facts.add(fact)

        result.semantic_facts = all_facts
        result.total_facts = len(all_facts)

        # Step 3: Extract related entity UUIDs from edges, only fetch information for these entities (not all nodes)
        entity_uuids = set()
        for edge_data in all_edges:
            if isinstance(edge_data, dict):
                source_uuid = edge_data.get('source_node_uuid', '')
                target_uuid = edge_data.get('target_node_uuid', '')
                if source_uuid:
                    entity_uuids.add(source_uuid)
                if target_uuid:
                    entity_uuids.add(target_uuid)

        # Get details for all related entities (no quantity limit, full output)
        entity_insights = []
        node_map = {}  # Used for relationship chain construction later

        for uuid in list(entity_uuids):  # Process all entities, no truncation
            if not uuid:
                continue
            try:
                # Fetch information for each related node individually
                node = self.get_node_detail(graph_id, uuid)
                if node:
                    node_map[uuid] = node
                    entity_type = next((l for l in node.labels if l not in ["Entity", "Node"]), "Entity")

                    # Get all facts related to this entity (no truncation)
                    related_facts = [
                        f for f in all_facts
                        if node.name.lower() in f.lower()
                    ]

                    entity_insights.append({
                        "uuid": node.uuid,
                        "name": node.name,
                        "type": entity_type,
                        "summary": node.summary,
                        "related_facts": related_facts  # Full output, no truncation
                    })
            except Exception as e:
                logger.debug(f"Failed to fetch node {uuid}: {e}")
                continue

        result.entity_insights = entity_insights
        result.total_entities = len(entity_insights)

        # Step 4: Build all relationship chains (no quantity limit)
        relationship_chains = []
        for edge_data in all_edges:  # Process all edges, no truncation
            if isinstance(edge_data, dict):
                source_uuid = edge_data.get('source_node_uuid', '')
                target_uuid = edge_data.get('target_node_uuid', '')
                relation_name = edge_data.get('name', '')

                source_name = node_map.get(source_uuid, NodeInfo('', '', [], '', {})).name or source_uuid[:8]
                target_name = node_map.get(target_uuid, NodeInfo('', '', [], '', {})).name or target_uuid[:8]

                chain = f"{source_name} --[{relation_name}]--> {target_name}"
                if chain not in relationship_chains:
                    relationship_chains.append(chain)

        result.relationship_chains = relationship_chains
        result.total_relationships = len(relationship_chains)

        logger.info(f"InsightForge completed: {result.total_facts} facts, {result.total_entities} entities, {result.total_relationships} relationships")
        return result

    def _generate_sub_queries(
        self,
        query: str,
        simulation_requirement: str,
        report_context: str = "",
        max_queries: int = 5
    ) -> List[str]:
        """
        Use LLM to generate sub-queries

        Decomposes a complex question into multiple sub-queries that can be independently retrieved.
        """
        system_prompt = """You are a professional problem analysis expert. Your task is to decompose a complex question into multiple sub-questions that can be independently observed in a simulated world.

Requirements:
1. Each sub-question should be specific enough to find relevant agent behaviors or events in the simulated world
2. Sub-questions should cover different dimensions of the original question (e.g., who, what, why, how, when, where)
3. Sub-questions should be relevant to the simulation scenario
4. Return in JSON format: {"sub_queries": ["sub-question 1", "sub-question 2", ...]}"""

        user_prompt = f"""Simulation requirement background:
{simulation_requirement}

{f"Report context: {report_context[:500]}" if report_context else ""}

Please decompose the following question into {max_queries} sub-questions:
{query}

Return the sub-question list in JSON format."""

        try:
            response = self.llm.chat_json(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3
            )

            sub_queries = response.get("sub_queries", [])
            # Ensure it's a list of strings
            return [str(sq) for sq in sub_queries[:max_queries]]

        except Exception as e:
            logger.warning(f"Failed to generate sub-queries: {str(e)}, using default sub-queries")
            # Fallback: return variants based on the original query
            return [
                query,
                f"Key participants in {query}",
                f"Causes and effects of {query}",
                f"Development process of {query}"
            ][:max_queries]

    def panorama_search(
        self,
        graph_id: str,
        query: str,
        include_expired: bool = True,
        limit: int = 50
    ) -> PanoramaResult:
        """
        [PanoramaSearch - Broad Search]

        Get the full panoramic view, including all relevant content and historical/expired information:
        1. Get all related nodes
        2. Get all edges (including expired/invalidated ones)
        3. Categorize and organize currently valid and historical information

        This tool is suitable for scenarios that require understanding the full picture of events and tracking their evolution.

        Args:
            graph_id: Graph ID
            query: Search query (used for relevance ranking)
            include_expired: Whether to include expired content (default True)
            limit: Result quantity limit

        Returns:
            PanoramaResult: Broad search result
        """
        logger.info(f"PanoramaSearch broad search: {query[:50]}...")

        result = PanoramaResult(query=query)

        # Get all nodes
        all_nodes = self.get_all_nodes(graph_id)
        node_map = {n.uuid: n for n in all_nodes}
        result.all_nodes = all_nodes
        result.total_nodes = len(all_nodes)

        # Get all edges (with temporal information)
        all_edges = self.get_all_edges(graph_id, include_temporal=True)
        result.all_edges = all_edges
        result.total_edges = len(all_edges)

        # Categorize facts
        active_facts = []
        historical_facts = []

        for edge in all_edges:
            if not edge.fact:
                continue

            # Add entity names to facts
            source_name = node_map.get(edge.source_node_uuid, NodeInfo('', '', [], '', {})).name or edge.source_node_uuid[:8]
            target_name = node_map.get(edge.target_node_uuid, NodeInfo('', '', [], '', {})).name or edge.target_node_uuid[:8]

            # Determine if expired/invalidated
            is_historical = edge.is_expired or edge.is_invalid

            if is_historical:
                # Historical/expired fact, add time markers
                valid_at = edge.valid_at or "Unknown"
                invalid_at = edge.invalid_at or edge.expired_at or "Unknown"
                fact_with_time = f"[{valid_at} - {invalid_at}] {edge.fact}"
                historical_facts.append(fact_with_time)
            else:
                # Currently valid fact
                active_facts.append(edge.fact)

        # Relevance-based sorting
        query_lower = query.lower()
        keywords = [w.strip() for w in query_lower.replace(',', ' ').replace('，', ' ').split() if len(w.strip()) > 1]

        def relevance_score(fact: str) -> int:
            fact_lower = fact.lower()
            score = 0
            if query_lower in fact_lower:
                score += 100
            for kw in keywords:
                if kw in fact_lower:
                    score += 10
            return score

        # Sort and limit quantity
        active_facts.sort(key=relevance_score, reverse=True)
        historical_facts.sort(key=relevance_score, reverse=True)

        result.active_facts = active_facts[:limit]
        result.historical_facts = historical_facts[:limit] if include_expired else []
        result.active_count = len(active_facts)
        result.historical_count = len(historical_facts)

        logger.info(f"PanoramaSearch completed: {result.active_count} active, {result.historical_count} historical")
        return result

    def quick_search(
        self,
        graph_id: str,
        query: str,
        limit: int = 10
    ) -> SearchResult:
        """
        [QuickSearch - Simple Search]

        Fast, lightweight retrieval tool:
        1. Directly calls graph search
        2. Returns the most relevant results
        3. Suitable for simple, direct retrieval needs

        Args:
            graph_id: Graph ID
            query: Search query
            limit: Number of results to return

        Returns:
            SearchResult: Search results
        """
        logger.info(f"QuickSearch simple search: {query[:50]}...")

        # Directly call the existing search_graph method
        result = self.search_graph(
            graph_id=graph_id,
            query=query,
            limit=limit,
            scope="edges"
        )

        logger.info(f"QuickSearch completed: {result.total_count} results")
        return result

    def interview_agents(
        self,
        simulation_id: str,
        interview_requirement: str,
        simulation_requirement: str = "",
        max_agents: int = 5,
        custom_questions: List[str] = None
    ) -> InterviewResult:
        """
        [InterviewAgents - In-Depth Interview]

        Calls the real OASIS interview API to interview agents running in the simulation:
        1. Automatically reads profile files to learn about all simulated agents
        2. Uses LLM to analyze interview requirements and intelligently select the most relevant agents
        3. Uses LLM to generate interview questions
        4. Calls /api/simulation/interview/batch endpoint for real interviews (dual-platform simultaneous interviews)
        5. Integrates all interview results and generates an interview report

        [Important] This feature requires the simulation environment to be running (OASIS environment not shut down)

        [Use Cases]
        - Need to understand event perspectives from different roles
        - Need to collect opinions and viewpoints from multiple parties
        - Need to obtain real responses from simulated agents (not LLM-simulated)

        Args:
            simulation_id: Simulation ID (used to locate profile files and call interview API)
            interview_requirement: Interview requirement description (unstructured, e.g., "understand students' views on the event")
            simulation_requirement: Simulation requirement background (optional)
            max_agents: Maximum number of agents to interview
            custom_questions: Custom interview questions (optional, auto-generated if not provided)

        Returns:
            InterviewResult: Interview result
        """
        from .simulation_runner import SimulationRunner

        logger.info(f"InterviewAgents in-depth interview (real API): {interview_requirement[:50]}...")

        result = InterviewResult(
            interview_topic=interview_requirement,
            interview_questions=custom_questions or []
        )

        # Step 1: Read profile files
        profiles = self._load_agent_profiles(simulation_id)

        if not profiles:
            logger.warning(f"No profile files found for simulation {simulation_id}")
            result.summary = "No agent profile files found for interview"
            return result

        result.total_agents = len(profiles)
        logger.info(f"Loaded {len(profiles)} agent profiles")

        # Step 2: Use LLM to select agents to interview (returns agent_id list)
        selected_agents, selected_indices, selection_reasoning = self._select_agents_for_interview(
            profiles=profiles,
            interview_requirement=interview_requirement,
            simulation_requirement=simulation_requirement,
            max_agents=max_agents
        )

        result.selected_agents = selected_agents
        result.selection_reasoning = selection_reasoning
        logger.info(f"Selected {len(selected_agents)} agents for interview: {selected_indices}")

        # Step 3: Generate interview questions (if not provided)
        if not result.interview_questions:
            result.interview_questions = self._generate_interview_questions(
                interview_requirement=interview_requirement,
                simulation_requirement=simulation_requirement,
                selected_agents=selected_agents
            )
            logger.info(f"Generated {len(result.interview_questions)} interview questions")

        # Combine questions into a single interview prompt
        combined_prompt = "\n".join([f"{i+1}. {q}" for i, q in enumerate(result.interview_questions)])

        # Add optimization prefix to constrain agent response format
        INTERVIEW_PROMPT_PREFIX = (
            "You are being interviewed. Please draw on your persona, all past memories, and actions "
            "to answer the following questions directly in plain text.\n"
            "Response requirements:\n"
            "1. Answer directly in natural language; do not call any tools\n"
            "2. Do not return JSON format or tool call format\n"
            "3. Do not use Markdown headings (such as #, ##, ###)\n"
            "4. Answer each question in order, starting each answer with 'Question X:' (where X is the question number)\n"
            "5. Separate answers to each question with a blank line\n"
            "6. Provide substantive answers, with at least 2-3 sentences per question\n\n"
        )
        optimized_prompt = f"{INTERVIEW_PROMPT_PREFIX}{combined_prompt}"

        # Step 4: Call the real interview API (no platform specified, defaults to dual-platform interview)
        try:
            # Build batch interview list (no platform specified, dual-platform interview)
            interviews_request = []
            for agent_idx in selected_indices:
                interviews_request.append({
                    "agent_id": agent_idx,
                    "prompt": optimized_prompt  # Use optimized prompt
                    # No platform specified, API will interview on both Twitter and Reddit
                })

            logger.info(f"Calling batch interview API (dual-platform): {len(interviews_request)} agents")

            # Call SimulationRunner's batch interview method (no platform passed, dual-platform interview)
            api_result = SimulationRunner.interview_agents_batch(
                simulation_id=simulation_id,
                interviews=interviews_request,
                platform=None,  # No platform specified, dual-platform interview
                timeout=180.0   # Dual-platform needs longer timeout
            )

            logger.info(f"Interview API returned: {api_result.get('interviews_count', 0)} results, success={api_result.get('success')}")

            # Check if API call was successful
            if not api_result.get("success", False):
                error_msg = api_result.get("error", "Unknown error")
                logger.warning(f"Interview API returned failure: {error_msg}")
                result.summary = f"Interview API call failed: {error_msg}. Please check the OASIS simulation environment status."
                return result

            # Step 5: Parse API return results and build AgentInterview objects
            # Dual-platform mode return format: {"twitter_0": {...}, "reddit_0": {...}, "twitter_1": {...}, ...}
            api_data = api_result.get("result", {})
            results_dict = api_data.get("results", {}) if isinstance(api_data, dict) else {}

            for i, agent_idx in enumerate(selected_indices):
                agent = selected_agents[i]
                agent_name = agent.get("realname", agent.get("username", f"Agent_{agent_idx}"))
                agent_role = agent.get("profession", "Unknown")
                agent_bio = agent.get("bio", "")

                # Get interview results for this agent on both platforms
                twitter_result = results_dict.get(f"twitter_{agent_idx}", {})
                reddit_result = results_dict.get(f"reddit_{agent_idx}", {})

                twitter_response = twitter_result.get("response", "")
                reddit_response = reddit_result.get("response", "")

                # Clean possible tool call JSON wrappers
                twitter_response = self._clean_tool_call_response(twitter_response)
                reddit_response = self._clean_tool_call_response(reddit_response)

                # Always output dual-platform markers
                twitter_text = twitter_response if twitter_response else "(No response from this platform)"
                reddit_text = reddit_response if reddit_response else "(No response from this platform)"
                response_text = f"[Twitter Platform Response]\n{twitter_text}\n\n[Reddit Platform Response]\n{reddit_text}"

                # Extract key quotes (from responses on both platforms)
                import re
                combined_responses = f"{twitter_response} {reddit_response}"

                # Clean response text: remove markers, numbering, Markdown, and other noise
                clean_text = re.sub(r'#{1,6}\s+', '', combined_responses)
                clean_text = re.sub(r'\{[^}]*tool_name[^}]*\}', '', clean_text)
                clean_text = re.sub(r'[*_`|>~\-]{2,}', '', clean_text)
                # Remove question markers in both Chinese ("问题" = "Question") and English
                clean_text = re.sub(r'(?:问题|Question)\s*\d+[：:]\s*', '', clean_text)
                clean_text = re.sub(r'【[^】]+】', '', clean_text)  # Remove Chinese bracket markers 【...】

                # Strategy 1 (primary): Extract complete sentences with substantive content
                sentences = re.split(r'[。！？.!?]', clean_text)
                meaningful = [
                    s.strip() for s in sentences
                    if 20 <= len(s.strip()) <= 150
                    and not re.match(r'^[\s\W，,；;：:、]+', s.strip())
                    and not s.strip().startswith(('{', '问题', 'Question'))  # "问题" = Chinese for "Question"
                ]
                meaningful.sort(key=len, reverse=True)
                key_quotes = [s + "。" for s in meaningful[:3]]  # "。" = Chinese full-stop period

                # Strategy 2 (supplementary): Correctly paired Chinese quotation marks with long text
                if not key_quotes:
                    paired = re.findall(r'\u201c([^\u201c\u201d]{15,100})\u201d', clean_text)
                    paired += re.findall(r'\u300c([^\u300c\u300d]{15,100})\u300d', clean_text)
                    key_quotes = [q for q in paired if not re.match(r'^[，,；;：:、]', q)][:3]

                interview = AgentInterview(
                    agent_name=agent_name,
                    agent_role=agent_role,
                    agent_bio=agent_bio[:1000],  # Extended bio length limit
                    question=combined_prompt,
                    response=response_text,
                    key_quotes=key_quotes[:5]
                )
                result.interviews.append(interview)

            result.interviewed_count = len(result.interviews)

        except ValueError as e:
            # Simulation environment not running
            logger.warning(f"Interview API call failed (environment not running?): {e}")
            result.summary = f"Interview failed: {str(e)}. The simulation environment may have been shut down. Please ensure the OASIS environment is running."
            return result
        except Exception as e:
            logger.error(f"Interview API call exception: {e}")
            import traceback
            logger.error(traceback.format_exc())
            result.summary = f"An error occurred during the interview: {str(e)}"
            return result

        # Step 6: Generate interview summary
        if result.interviews:
            result.summary = self._generate_interview_summary(
                interviews=result.interviews,
                interview_requirement=interview_requirement
            )

        logger.info(f"InterviewAgents completed: interviewed {result.interviewed_count} agents (dual-platform)")
        return result

    @staticmethod
    def _clean_tool_call_response(response: str) -> str:
        """Clean JSON tool call wrappers from agent responses and extract actual content"""
        if not response or not response.strip().startswith('{'):
            return response
        text = response.strip()
        if 'tool_name' not in text[:80]:
            return response
        import re as _re
        try:
            data = json.loads(text)
            if isinstance(data, dict) and 'arguments' in data:
                for key in ('content', 'text', 'body', 'message', 'reply'):
                    if key in data['arguments']:
                        return str(data['arguments'][key])
        except (json.JSONDecodeError, KeyError, TypeError):
            match = _re.search(r'"content"\s*:\s*"((?:[^"\\]|\\.)*)"', text)
            if match:
                return match.group(1).replace('\\n', '\n').replace('\\"', '"')
        return response

    def _load_agent_profiles(self, simulation_id: str) -> List[Dict[str, Any]]:
        """Load agent profile files for the simulation"""
        import os
        import csv

        # Build profile file path
        sim_dir = os.path.join(
            os.path.dirname(__file__),
            f'../../uploads/simulations/{simulation_id}'
        )

        profiles = []

        # Prefer reading Reddit JSON format
        reddit_profile_path = os.path.join(sim_dir, "reddit_profiles.json")
        if os.path.exists(reddit_profile_path):
            try:
                with open(reddit_profile_path, 'r', encoding='utf-8') as f:
                    profiles = json.load(f)
                logger.info(f"Loaded {len(profiles)} profiles from reddit_profiles.json")
                return profiles
            except Exception as e:
                logger.warning(f"Failed to read reddit_profiles.json: {e}")

        # Try reading Twitter CSV format
        twitter_profile_path = os.path.join(sim_dir, "twitter_profiles.csv")
        if os.path.exists(twitter_profile_path):
            try:
                with open(twitter_profile_path, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # Convert CSV format to unified format
                        profiles.append({
                            "realname": row.get("name", ""),
                            "username": row.get("username", ""),
                            "bio": row.get("description", ""),
                            "persona": row.get("user_char", ""),
                            "profession": "Unknown"
                        })
                logger.info(f"Loaded {len(profiles)} profiles from twitter_profiles.csv")
                return profiles
            except Exception as e:
                logger.warning(f"Failed to read twitter_profiles.csv: {e}")

        return profiles

    def _select_agents_for_interview(
        self,
        profiles: List[Dict[str, Any]],
        interview_requirement: str,
        simulation_requirement: str,
        max_agents: int
    ) -> tuple:
        """
        Use LLM to select agents to interview

        Returns:
            tuple: (selected_agents, selected_indices, reasoning)
                - selected_agents: Full information list of selected agents
                - selected_indices: Index list of selected agents (for API calls)
                - reasoning: Selection reasoning
        """

        # Build agent summary list
        agent_summaries = []
        for i, profile in enumerate(profiles):
            summary = {
                "index": i,
                "name": profile.get("realname", profile.get("username", f"Agent_{i}")),
                "profession": profile.get("profession", "Unknown"),
                "bio": profile.get("bio", "")[:200],
                "interested_topics": profile.get("interested_topics", [])
            }
            agent_summaries.append(summary)

        system_prompt = """You are a professional interview planning expert. Your task is to select the most suitable interview subjects from a list of simulated agents based on interview requirements.

Selection criteria:
1. The agent's identity/profession is relevant to the interview topic
2. The agent may hold unique or valuable perspectives
3. Select diverse viewpoints (e.g., supporters, opponents, neutral parties, professionals, etc.)
4. Prioritize roles directly related to the event

Return in JSON format:
{
    "selected_indices": [list of selected agent indices],
    "reasoning": "Explanation of selection reasoning"
}"""

        user_prompt = f"""Interview requirement:
{interview_requirement}

Simulation background:
{simulation_requirement if simulation_requirement else "Not provided"}

Available agent list ({len(agent_summaries)} total):
{json.dumps(agent_summaries, ensure_ascii=False, indent=2)}

Please select up to {max_agents} agents most suitable for interview and explain the selection reasoning."""

        try:
            response = self.llm.chat_json(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3
            )

            selected_indices = response.get("selected_indices", [])[:max_agents]
            reasoning = response.get("reasoning", "Automatically selected based on relevance")

            # Get full information of selected agents
            selected_agents = []
            valid_indices = []
            for idx in selected_indices:
                if 0 <= idx < len(profiles):
                    selected_agents.append(profiles[idx])
                    valid_indices.append(idx)

            return selected_agents, valid_indices, reasoning

        except Exception as e:
            logger.warning(f"LLM agent selection failed, using default selection: {e}")
            # Fallback: select the first N agents
            selected = profiles[:max_agents]
            indices = list(range(min(max_agents, len(profiles))))
            return selected, indices, "Using default selection strategy"

    def _generate_interview_questions(
        self,
        interview_requirement: str,
        simulation_requirement: str,
        selected_agents: List[Dict[str, Any]]
    ) -> List[str]:
        """Use LLM to generate interview questions"""

        agent_roles = [a.get("profession", "Unknown") for a in selected_agents]

        system_prompt = """You are a professional journalist/interviewer. Generate 3-5 in-depth interview questions based on the interview requirements.

Question requirements:
1. Open-ended questions that encourage detailed responses
2. Questions that different roles might answer differently
3. Cover multiple dimensions including facts, opinions, and feelings
4. Natural language, like a real interview
5. Keep each question under 50 words, concise and clear
6. Ask directly, do not include background descriptions or prefixes

Return in JSON format: {"questions": ["question 1", "question 2", ...]}"""

        user_prompt = f"""Interview requirement: {interview_requirement}

Simulation background: {simulation_requirement if simulation_requirement else "Not provided"}

Interviewee roles: {', '.join(agent_roles)}

Please generate 3-5 interview questions."""

        try:
            response = self.llm.chat_json(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.5
            )

            return response.get("questions", [f"What are your thoughts on {interview_requirement}?"])

        except Exception as e:
            logger.warning(f"Failed to generate interview questions: {e}")
            return [
                f"What is your perspective on {interview_requirement}?",
                "What impact does this have on you or the group you represent?",
                "How do you think this issue should be resolved or improved?"
            ]

    def _generate_interview_summary(
        self,
        interviews: List[AgentInterview],
        interview_requirement: str
    ) -> str:
        """Generate interview summary"""

        if not interviews:
            return "No interviews were completed"

        # Collect all interview content
        interview_texts = []
        for interview in interviews:
            interview_texts.append(f"[{interview.agent_name} ({interview.agent_role})]\n{interview.response[:500]}")

        system_prompt = """You are a professional news editor. Based on responses from multiple interviewees, generate an interview summary.

Summary requirements:
1. Distill the main viewpoints from each party
2. Identify areas of consensus and disagreement
3. Highlight valuable quotes
4. Remain objective and neutral, without favoring any side
5. Keep within 1000 words

Format constraints (must be followed):
- Use plain text paragraphs, separated by blank lines
- Do not use Markdown headings (such as #, ##, ###)
- Do not use divider lines (such as ---, ***)
- When quoting interviewees, use quotation marks
- You may use **bold** to mark keywords, but do not use other Markdown syntax"""

        user_prompt = f"""Interview topic: {interview_requirement}

Interview content:
{"".join(interview_texts)}

Please generate an interview summary."""

        try:
            summary = self.llm.chat(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
                max_tokens=800
            )
            return summary

        except Exception as e:
            logger.warning(f"Failed to generate interview summary: {e}")
            # Fallback: simple concatenation
            return f"A total of {len(interviews)} interviewees were interviewed, including: " + ", ".join([i.agent_name for i in interviews])


KuzuToolsService = GraphToolsService
