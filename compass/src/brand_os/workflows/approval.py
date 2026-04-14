"""Approval workflow state machine for decision review.

Uses python-statemachine for state transitions with audit logging.
Falls back to manual state management if statemachine not installed.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from brand_os.core.config import utc_now
from brand_os.core.decision import (
    Decision,
    DecisionStatus,
    get_decision,
    get_decision_log,
)

# Try to import statemachine, fall back to manual implementation
try:
    from statemachine import State, StateMachine

    STATEMACHINE_AVAILABLE = True
except ImportError:
    STATEMACHINE_AVAILABLE = False
    StateMachine = object  # type: ignore
    State = None  # type: ignore


if STATEMACHINE_AVAILABLE:

    class ApprovalWorkflow(StateMachine):
        """State machine for decision approval workflow.

        States:
            draft -> pending_review -> approved -> executed
                                   -> rejected

        Transitions are logged to the decision audit trail.
        """

        # States
        draft = State(initial=True)
        pending_review = State()
        approved = State()
        rejected = State()
        executed = State(final=True)
        failed = State(final=True)

        # Transitions
        submit = draft.to(pending_review)
        approve = pending_review.to(approved)
        reject = pending_review.to(rejected)
        execute = approved.to(executed)
        fail = approved.to(failed) | executed.to(failed)

        def __init__(self, decision: Decision, **kwargs: Any):
            self.decision = decision
            # Map decision status to state
            state_map = {
                DecisionStatus.DRAFT: self.draft,
                DecisionStatus.PENDING_REVIEW: self.pending_review,
                DecisionStatus.APPROVED: self.approved,
                DecisionStatus.REJECTED: self.rejected,
                DecisionStatus.EXECUTED: self.executed,
                DecisionStatus.FAILED: self.failed,
            }
            initial_state = state_map.get(decision.status, self.draft)
            super().__init__(start_value=initial_state, **kwargs)

        def on_enter_pending_review(self) -> None:
            """Called when decision enters pending_review state."""
            self.decision.status = DecisionStatus.PENDING_REVIEW
            self._save()
            self._notify("Decision submitted for review")

        def on_enter_approved(self, reviewer: str = "unknown", reason: str = "") -> None:
            """Called when decision is approved."""
            self.decision.status = DecisionStatus.APPROVED
            self.decision.reviewer = reviewer
            self.decision.review_reason = reason
            self.decision.reviewed_at = utc_now()
            self._save()
            self._notify(f"Decision approved by {reviewer}")

        def on_enter_rejected(self, reviewer: str = "unknown", reason: str = "") -> None:
            """Called when decision is rejected."""
            self.decision.status = DecisionStatus.REJECTED
            self.decision.reviewer = reviewer
            self.decision.review_reason = reason
            self.decision.reviewed_at = utc_now()
            self._save()
            self._notify(f"Decision rejected by {reviewer}: {reason}")

        def on_enter_executed(self, outcome: dict[str, Any] | None = None) -> None:
            """Called when decision is executed."""
            self.decision.status = DecisionStatus.EXECUTED
            self.decision.executed_at = utc_now()
            self.decision.outcome = outcome
            self._save()

        def on_enter_failed(self, error: str = "") -> None:
            """Called when execution fails."""
            self.decision.status = DecisionStatus.FAILED
            self.decision.error = error
            self._save()

        def _save(self) -> None:
            """Persist decision state."""
            get_decision_log().update(self.decision)

        def _notify(self, message: str) -> None:
            """Send notification (placeholder for Slack/email integration)."""
            # TODO: Implement notification via slack-sdk or email
            pass

else:
    # Fallback implementation without statemachine dependency

    class ApprovalWorkflow:  # type: ignore[no-redef]
        """Manual state machine implementation (fallback)."""

        VALID_TRANSITIONS = {
            DecisionStatus.DRAFT: [DecisionStatus.PENDING_REVIEW],
            DecisionStatus.PENDING_REVIEW: [DecisionStatus.APPROVED, DecisionStatus.REJECTED],
            DecisionStatus.APPROVED: [DecisionStatus.EXECUTED, DecisionStatus.FAILED],
            DecisionStatus.EXECUTED: [DecisionStatus.FAILED],
            DecisionStatus.REJECTED: [],
            DecisionStatus.FAILED: [],
        }

        def __init__(self, decision: Decision):
            self.decision = decision

        def _transition(self, new_status: DecisionStatus) -> None:
            valid = self.VALID_TRANSITIONS.get(self.decision.status, [])
            if new_status not in valid:
                raise ValueError(
                    f"Invalid transition: {self.decision.status} -> {new_status}"
                )
            self.decision.status = new_status
            self.decision.updated_at = utc_now()
            get_decision_log().update(self.decision)

        def submit(self) -> None:
            self._transition(DecisionStatus.PENDING_REVIEW)

        def approve(self, reviewer: str = "unknown", reason: str = "") -> None:
            self.decision.reviewer = reviewer
            self.decision.review_reason = reason
            self.decision.reviewed_at = utc_now()
            self._transition(DecisionStatus.APPROVED)

        def reject(self, reviewer: str = "unknown", reason: str = "") -> None:
            self.decision.reviewer = reviewer
            self.decision.review_reason = reason
            self.decision.reviewed_at = utc_now()
            self._transition(DecisionStatus.REJECTED)

        def execute(self, outcome: dict[str, Any] | None = None) -> None:
            self.decision.executed_at = utc_now()
            self.decision.outcome = outcome
            self._transition(DecisionStatus.EXECUTED)

        def fail(self, error: str = "") -> None:
            self.decision.error = error
            self._transition(DecisionStatus.FAILED)


# Convenience functions for CLI usage


def approve_decision(
    decision_id: str,
    reviewer: str,
    reason: str = "",
    brand: str | None = None,
) -> Decision | None:
    """Approve a pending decision."""
    decision = get_decision(decision_id, brand)
    if not decision:
        return None

    workflow = ApprovalWorkflow(decision)
    if STATEMACHINE_AVAILABLE:
        workflow.approve(reviewer=reviewer, reason=reason)
    else:
        workflow.approve(reviewer, reason)

    return decision


def reject_decision(
    decision_id: str,
    reviewer: str,
    reason: str,
    brand: str | None = None,
) -> Decision | None:
    """Reject a pending decision."""
    decision = get_decision(decision_id, brand)
    if not decision:
        return None

    workflow = ApprovalWorkflow(decision)
    if STATEMACHINE_AVAILABLE:
        workflow.reject(reviewer=reviewer, reason=reason)
    else:
        workflow.reject(reviewer, reason)

    return decision


def submit_for_review(decision: Decision) -> Decision:
    """Submit a draft decision for review."""
    workflow = ApprovalWorkflow(decision)
    workflow.submit()
    return decision


def execute_decision(
    decision_id: str,
    outcome: dict[str, Any] | None = None,
    brand: str | None = None,
) -> Decision | None:
    """Mark an approved decision as executed."""
    decision = get_decision(decision_id, brand)
    if not decision:
        return None

    workflow = ApprovalWorkflow(decision)
    if STATEMACHINE_AVAILABLE:
        workflow.execute(outcome=outcome)
    else:
        workflow.execute(outcome)

    return decision
