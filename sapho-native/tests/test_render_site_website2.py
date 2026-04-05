from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import render_site


class RenderSiteWebsite2Tests(unittest.TestCase):
    def test_site_mode_and_feeds_default_for_github_pages(self) -> None:
        with patch.dict(os.environ, {"SAPHO_SITE_MODE": "github-pages"}, clear=False):
            self.assertEqual(render_site.site_mode(), "github-pages")
            self.assertFalse(render_site.site_feeds_enabled())

    def test_site_custom_domain_defaults_from_base_url(self) -> None:
        with patch.dict(os.environ, {"SAPHO_SITE_BASE_URL": "https://research.quiznat.com"}, clear=False):
            self.assertEqual(render_site.site_custom_domain(), "research.quiznat.com")

    def test_apply_website2_surface_overrides_rebuilds_homepage_with_charter_and_kept_artifacts_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            public_dir = Path(tmpdir)
            with patch.object(render_site, "PUBLIC_DIR", public_dir), patch.dict(
                os.environ,
                {
                    "SAPHO_SITE_MODE": "github-pages",
                    "SAPHO_SITE_CUSTOM_DOMAIN": "research.quiznat.com",
                },
                clear=False,
            ):
                render_site.apply_website2_surface_overrides(
                    [
                        {
                            "title": "Fresh Lawful Artifact",
                            "summary": "Dense new artifact summary.",
                            "artifact_rel": "artifacts/kb/queue/fresh-lawful-artifact.md",
                            "url": "https://example.com/source",
                        }
                    ]
                )
            updated = (public_dir / "index.html").read_text(encoding="utf-8")
            self.assertIn("Institute Charter", updated)
            self.assertIn("Kept Artifact Index", updated)
            self.assertIn("Recent Kept Artifacts", updated)
            self.assertIn("Fresh Lawful Artifact", updated)
            self.assertNotIn("Latest Daily Briefing", updated)
            self.assertNotIn("Longform Research", updated)
            self.assertEqual((public_dir / "CNAME").read_text(encoding="utf-8").strip(), "research.quiznat.com")

    def test_reset_public_dir_requires_baseline_in_github_pages_mode(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            public_dir = Path(tmpdir)
            (public_dir / "assets").mkdir(parents=True, exist_ok=True)
            for rel in ["index.html", "viewer.html", "charter.html", "assets/style.css", "assets/sapho-seal.png"]:
                path = public_dir / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("ok", encoding="utf-8")
            with patch.object(render_site, "PUBLIC_DIR", public_dir), patch.dict(os.environ, {"SAPHO_SITE_MODE": "github-pages"}, clear=False):
                render_site.reset_public_dir()


if __name__ == "__main__":
    unittest.main()
