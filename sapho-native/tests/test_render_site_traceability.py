from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(ROOT))

import render_site


class RenderSiteTraceabilityTests(unittest.TestCase):
    def test_public_artifact_markdown_includes_traceability_panel(self) -> None:
        meta = {
            "source_url": "https://example.com/source",
            "queued_at_utc": "2026-04-04T00:00:00Z",
            "captured_at_utc": "2026-04-04T00:05:00Z",
            "curated_at_utc": "2026-04-04T00:10:00Z",
            "artifact_minted_at_utc": "2026-04-04T00:15:00Z",
            "artifact_publication_published_at_utc": "2026-04-04T00:20:00Z",
        }
        body = """---
version: article.v1
article_id: art-test-501
---
# Example Artifact

## Core Thesis

Traceability should be visible.
"""
        text = render_site.build_public_artifact_markdown("pub-001", "Example Artifact", meta, body)
        self.assertIn('<details class="traceability-panel">', text)
        self.assertIn('Traceability</summary>', text)
        self.assertIn('https://example.com/source', text)
        self.assertIn('Intake queued:', text)
        self.assertIn('Source captured:', text)
        self.assertIn('Curated:', text)
        self.assertIn('Artifact finalized:', text)
        self.assertIn('Artifact published:', text)
        self.assertIn('# Example Artifact', text)


if __name__ == "__main__":
    unittest.main()
