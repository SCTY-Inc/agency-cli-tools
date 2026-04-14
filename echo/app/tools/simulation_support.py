"""Shared simulation workflow helpers."""

import json
import os
from datetime import datetime
from typing import Any, Dict, Tuple

from ..config import Config
from ..utils.logger import get_logger

logger = get_logger("mirofish.tools.simulation_support")


def check_simulation_prepared(simulation_id: str) -> Tuple[bool, Dict[str, Any]]:
    """Check whether a simulation has all artifacts needed to run."""
    simulation_dir = os.path.join(Config.OASIS_SIMULATION_DATA_DIR, simulation_id)
    if not os.path.exists(simulation_dir):
        return False, {"reason": "Simulation directory does not exist"}

    required_files = [
        "state.json",
        "simulation_config.json",
        "reddit_profiles.json",
        "twitter_profiles.csv",
    ]

    existing_files = []
    missing_files = []
    for filename in required_files:
        path = os.path.join(simulation_dir, filename)
        if os.path.exists(path):
            existing_files.append(filename)
        else:
            missing_files.append(filename)

    if missing_files:
        return False, {
            "reason": "Missing required files",
            "missing_files": missing_files,
            "existing_files": existing_files,
        }

    state_file = os.path.join(simulation_dir, "state.json")
    try:
        with open(state_file, "r", encoding="utf-8") as f:
            state_data = json.load(f)

        status = state_data.get("status", "")
        config_generated = state_data.get("config_generated", False)
        prepared_statuses = ["ready", "preparing", "running", "completed", "stopped", "failed"]

        if status in prepared_statuses and config_generated:
            profiles_file = os.path.join(simulation_dir, "reddit_profiles.json")
            profiles_count = 0
            if os.path.exists(profiles_file):
                with open(profiles_file, "r", encoding="utf-8") as f:
                    profiles_data = json.load(f)
                    profiles_count = len(profiles_data) if isinstance(profiles_data, list) else 0

            if status == "preparing":
                try:
                    state_data["status"] = "ready"
                    state_data["updated_at"] = datetime.now().isoformat()
                    with open(state_file, "w", encoding="utf-8") as f:
                        json.dump(state_data, f, ensure_ascii=False, indent=2)
                    status = "ready"
                    logger.info(f"Auto-updated simulation status: {simulation_id} preparing -> ready")
                except Exception as exc:
                    logger.warning(f"Failed to auto-update simulation status: {exc}")

            return True, {
                "status": status,
                "entities_count": state_data.get("entities_count", 0),
                "profiles_count": profiles_count,
                "entity_types": state_data.get("entity_types", []),
                "config_generated": config_generated,
                "created_at": state_data.get("created_at"),
                "updated_at": state_data.get("updated_at"),
                "existing_files": existing_files,
            }

        return False, {
            "reason": f"Status not ready for run: status={status}, config_generated={config_generated}",
            "status": status,
            "config_generated": config_generated,
            "existing_files": existing_files,
        }
    except Exception as exc:
        return False, {"reason": f"Failed to read state file: {exc}"}
