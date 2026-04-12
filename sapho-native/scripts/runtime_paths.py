from __future__ import annotations

import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ROOT_ENV_VAR = "SAPHO_RUNTIME_ROOT"


def _resolve(path_value: str) -> Path:
    candidate = Path(path_value).expanduser()
    if not candidate.is_absolute():
        candidate = (PROJECT_ROOT / candidate).resolve()
    return candidate


def runtime_root() -> Path:
    configured = os.environ.get(RUNTIME_ROOT_ENV_VAR, "").strip()
    return _resolve(configured) if configured else (PROJECT_ROOT / "runtime")


PROJECT_ROOT_PATH = PROJECT_ROOT
RUNTIME_ROOT = runtime_root()
RUNTIME_RESEARCH_ROOT = RUNTIME_ROOT / "research"
RUNTIME_WEBSITE_ROOT = RUNTIME_ROOT / "website"
RUNTIME_ARTICLES_ROOT = RUNTIME_RESEARCH_ROOT / "articles"
RUNTIME_SOURCE_ROOT = RUNTIME_RESEARCH_ROOT / "source-material"
RUNTIME_DAILY_ROOT = RUNTIME_RESEARCH_ROOT / "publication" / "daily"
RUNTIME_FACTORY_CHECKIN_DIR = RUNTIME_RESEARCH_ROOT / "factory" / "checkins"
RUNTIME_FACTORY_CHECKIN_LATEST = RUNTIME_FACTORY_CHECKIN_DIR / "article-checkin-latest.json"
RUNTIME_REPORTS_SHIFTS = RUNTIME_RESEARCH_ROOT / "reports" / "shifts"