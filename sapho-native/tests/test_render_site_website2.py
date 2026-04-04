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

    def test_apply_website2_surface_overrides_removes_rss_and_writes_cname(self) -> None:
        homepage = """<!doctype html>
<html>
<head>
  <link rel=\"alternate\" type=\"application/rss+xml\" title=\"Artifacts RSS\" href=\"artifacts.xml\" />
</head>
<body>
  <h2>Machine Entry</h2>
  <article class=\"mentat-card report-card\">
    <h3><a href=\"artifacts.xml\">Artifacts RSS</a></h3>
    <p>Sequential artifact feed continuity for published research outputs.</p>
    <p class=\"meta\"><a href=\"artifacts.xml\">Open RSS</a></p>
  </article>
</body>
</html>
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            public_dir = Path(tmpdir)
            (public_dir / "index.html").write_text(homepage, encoding="utf-8")
            with patch.object(render_site, "PUBLIC_DIR", public_dir), patch.dict(
                os.environ,
                {
                    "SAPHO_SITE_MODE": "github-pages",
                    "SAPHO_SITE_CUSTOM_DOMAIN": "research.quiznat.com",
                },
                clear=False,
            ):
                render_site.apply_website2_surface_overrides()
            updated = (public_dir / "index.html").read_text(encoding="utf-8")
            self.assertNotIn("Artifacts RSS", updated)
            self.assertIn("Machine Entry and Operations", updated)
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
