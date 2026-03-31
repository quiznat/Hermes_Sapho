from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import common
import micro_common


class MicroCommonPathTests(unittest.TestCase):
    def test_article_stage_path_uses_runtime_articles_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            articles_dir = Path(tmpdir) / "articles"
            with patch.object(common, "ARTICLES_DIR", articles_dir):
                self.assertEqual(
                    micro_common.article_stage_path("art-test-201", "facts"),
                    articles_dir / "art-test-201" / "micro-facts.md",
                )

    def test_daily_stage_path_uses_runtime_daily_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            daily_dir = Path(tmpdir) / "daily"
            with patch.object(common, "DAILY_DIR", daily_dir):
                self.assertEqual(
                    micro_common.daily_stage_path("2026-03-31", "executive"),
                    daily_dir / "2026-03-31" / "micro-executive.md",
                )


if __name__ == "__main__":
    unittest.main()
