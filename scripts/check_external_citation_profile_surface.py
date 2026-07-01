#!/usr/bin/env python3
"""Check the profile external-citation routing surface.

The check is intentionally text-based: this repository is a public routing
surface, so the main risk is broken agent-readable routing or overclaiming.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "README.md": [
        "External reuse / citation entry",
        "verifiable-tool-invocation-flow",
        "persona-object-protocol",
        "docs/external-citation-front-door-2026-06-28.md",
        "docs/external-citation-route-manifest.json",
        "not official framework integrations",
    ],
    "llms.txt": [
        "external-citation-front-door",
        "external-citation-route-manifest",
        "tool-call receipt problem",
        "post-execution receipt review problem",
        "portable persona config problem",
        "Do not describe these routes as official",
    ],
    "docs/external-citation-front-door-2026-06-28.md": [
        "status: local profile routing candidate, not pushed, not posted.",
        "current_profile_changes_public: false.",
        "Verify one agent tool call outside the original runtime",
        "current_truth_surface: local `joy7758` profile worktree only.",
        "Machine-readable route manifest: `docs/external-citation-route-manifest.json`.",
        "PROFILE_EXTERNAL_CITATION_SURFACE_OK",
    ],
    "docs/external-citation-route-manifest.json": [
        '"status": "local_profile_route_manifest_candidate_only"',
        '"route_count": 4',
        '"external_citation_evidence_recorded": false',
        '"goal_completion_candidate": false',
        '"route_id": "tool_call_receipt"',
        '"route_id": "receipt_review"',
        '"route_id": "portable_persona_config"',
        '"route_id": "agent_run_audit_json"',
    ],
    "docs/outbound-entry-priority.md": [
        "verifiable-tool-invocation-flow",
        "docs/external-citation-front-door-2026-06-28.md",
    ],
    "docs/pinned-front-door-final.md": [
        "External citation campaign variant",
        "verifiable-tool-invocation-flow",
        "routing recommendation only",
    ],
    "docs/public-surface-ops-checklist.md": [
        "external citation campaign variant",
        "verifiable-tool-invocation-flow",
    ],
}

FORBIDDEN_CLAIMS = [
    "official LangChain integration",
    "official CrewAI integration",
    "official AutoGen integration",
    "is compliance certification",
    "provides compliance certification",
    "is legal non-repudiation",
    "provides legal non-repudiation",
    "is an externally validated integration",
    "is externally validated integration",
    "provides externally validated integration",
    "is production forensic timestamping",
    "provides production forensic timestamping",
]

LIGHTWEIGHT_LINE_LIMITS = {
    "README.md": 190,
    "llms.txt": 80,
    "AGENTS.md": 80,
    "docs/external-citation-front-door-2026-06-28.md": 90,
}

LIGHTWEIGHT_REQUIRED = {
    "AGENTS.md": [
        "public identity and routing surface",
        "not the runtime implementation",
        "Do not duplicate the full architecture hub index",
        "Do not modify `tse_transfer/` unless the user explicitly asks",
    ],
    "README.md": [
        "这个 Profile 是公开身份和项目路由入口",
        "Boundary: these are public routing and reuse surfaces",
    ],
    "llms.txt": [
        "It is a public identity and project routing surface",
        "not the runtime implementation or canonical architecture index",
    ],
}

FORBIDDEN_RUNTIME_SURFACE_SNIPPETS = [
    "pip install ",
    "npm install",
    "docker run",
    "docker compose",
    "kubectl ",
    "terraform ",
    "gh pr create",
    "gh release",
    "twine upload",
    "publish to pypi",
    "deploy to production",
]


def read_required(path: str) -> str:
    full_path = ROOT / path
    if not full_path.exists():
        raise SystemExit(f"missing required file: {path}")
    return full_path.read_text(encoding="utf-8")


def ensure_lightweight_profile_surface() -> None:
    """Keep this profile repo as routing metadata, not a runtime command hub."""
    for path, limit in LIGHTWEIGHT_LINE_LIMITS.items():
        text = read_required(path)
        line_count = len(text.splitlines())
        if line_count > limit:
            raise SystemExit(f"{path} is too large for a lightweight profile route: {line_count} > {limit}")

    for path, snippets in LIGHTWEIGHT_REQUIRED.items():
        text = read_required(path)
        for snippet in snippets:
            if snippet not in text:
                raise SystemExit(f"missing lightweight-routing snippet in {path}: {snippet}")

    for path in ("README.md", "llms.txt", "AGENTS.md"):
        lowered = read_required(path).lower()
        for snippet in FORBIDDEN_RUNTIME_SURFACE_SNIPPETS:
            if snippet in lowered:
                raise SystemExit(f"{path} must not become a runtime/package/release command surface: {snippet}")


def ensure_route_manifest() -> None:
    """Keep the profile routing manifest small, structured, and boundary-safe."""
    manifest_path = ROOT / "docs/external-citation-route-manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"route manifest JSON invalid: {exc}") from exc

    expected_top_level = {
        "status": "local_profile_route_manifest_candidate_only",
        "current_truth_surface": "local joy7758 profile worktree only",
        "current_profile_changes_public": False,
        "public_write_done": False,
        "external_citation_evidence_recorded": False,
        "goal_completion_candidate": False,
        "profile_front_door": "docs/external-citation-front-door-2026-06-28.md",
        "profile_ai_citation_card": "docs/start-here/ai-citation-card.md",
        "route_count": 4,
    }
    for field, expected in expected_top_level.items():
        if manifest.get(field) != expected:
            raise SystemExit(f"route manifest {field} must be {expected!r}")

    expected_routes = {
        "tool_call_receipt": (
            "verifiable-tool-invocation-flow",
            "verify-agent-tool-call-receipt.md",
            "guarded tool call -> signed receipt -> independent verifier",
        ),
        "receipt_review": (
            "aro-audit",
            "verify-one-receipt.md",
            "receipt fixture -> verifier -> audit/review status",
        ),
        "portable_persona_config": (
            "persona-object-protocol",
            "portable-persona-for-crewai.md",
            "persona object -> config export -> framework trial",
        ),
        "agent_run_audit_json": (
            "verifiable-agent-demo",
            "from-agent-run-to-audit-json.md",
            "agent run -> evidence bundle -> audit JSON",
        ),
    }
    routes = manifest.get("routes", [])
    if len(routes) != manifest.get("route_count"):
        raise SystemExit("route manifest route_count does not match routes length")
    by_id = {route.get("route_id"): route for route in routes}
    if set(by_id) != set(expected_routes):
        raise SystemExit("route manifest route IDs changed")
    for route_id, (repo, start_page, reuse_unit) in expected_routes.items():
        route = by_id[route_id]
        if route.get("first_repo") != repo:
            raise SystemExit(f"route manifest {route_id}.first_repo changed")
        if f"github.com/joy7758/{repo}" not in route.get("public_url_after_gate", ""):
            raise SystemExit(f"route manifest {route_id}.public_url_after_gate changed")
        if start_page not in route.get("start_here_after_gate", ""):
            raise SystemExit(f"route manifest {route_id}.start_here_after_gate changed")
        if "ai-citation-card.md" not in route.get("ai_citation_card_after_gate", ""):
            raise SystemExit(f"route manifest {route_id}.ai_citation_card_after_gate missing card")
        if route.get("citation_or_reuse_unit") != reuse_unit:
            raise SystemExit(f"route manifest {route_id}.citation_or_reuse_unit changed")
        triggers = route.get("query_triggers", [])
        if len(triggers) < 4 or not all(isinstance(item, str) and item for item in triggers):
            raise SystemExit(f"route manifest {route_id}.query_triggers must contain four text triggers")

    boundary = manifest.get("boundary", {})
    for field in (
        "not_official_framework_integration",
        "not_legal_non_repudiation",
        "not_compliance_certification",
        "not_external_validation",
        "not_ai_citation_evidence_until_third_party_url_recorded",
    ):
        if boundary.get(field) is not True:
            raise SystemExit(f"route manifest boundary.{field} must be true")


def main() -> None:
    combined = []
    for path, snippets in REQUIRED.items():
        text = read_required(path)
        combined.append(text)
        for snippet in snippets:
            if snippet not in text:
                raise SystemExit(f"missing snippet in {path}: {snippet}")

    all_text = "\n".join(combined)
    for claim in FORBIDDEN_CLAIMS:
        if claim in all_text:
            raise SystemExit(f"forbidden overclaim present: {claim}")

    ensure_lightweight_profile_surface()
    ensure_route_manifest()

    print("PROFILE_EXTERNAL_CITATION_SURFACE_OK")


if __name__ == "__main__":
    main()
