# Architecture

This document describes the current, binding architecture. It is maintained only through the
[`accept-adr`](../.github/prompts/accept-adr.prompt.md) prompt, except for the foundational entry
below, which describes the SpecPilot framework itself.

## The SpecPilot framework

SpecPilot is a spec-driven development framework, not an application. It has two parts:

- **`.github/` — the automation surface.** GitHub Copilot configuration that is loaded on demand:
  `copilot-instructions.md` (always-on, deliberately brief), the `spec-implementer` agent, the
  `spec-planner`, `spec-implementer`, `frontend-design` and `adr-writer` skills, the `accept-adr`
  and `pull-request` prompts, and the `docs/**` instructions. These encode the roles and gates of
  the workflow.
- **`docs/` — the human workspace.** An Obsidian vault holding feature specs (`docs/specs/`),
  Architecture Decision Records (`docs/adr/`), this architecture document, the project's design
  rules (`docs/design.md`, started from default rules), templates (`docs/_templates/`), and a
  `board.base` kanban view of specs by status.

### Agents, skills and prompts

- **Skills** hold procedures any agent can load on demand: planning (`spec-planner`), implementing
  (`spec-implementer`), UI work (`frontend-design`) and decisions (`adr-writer`). Planning is a
  skill so it can run inside a normal conversation; its plan-only boundary is an instruction, and
  the implementer's `planned` gate is the enforcement.
- **The `spec-implementer` agent** owns implementation. It combines the `spec-implementer` skill
  with `frontend-design` for UI steps. It never publishes; the user runs `pull-request`.
- **Prompts** are user-started, gated actions: `accept-adr` and `pull-request`.

### Workflow and roles

Work flows through fixed stages, each owned by one role with a narrow boundary:

1. A human writes a spec's `Description` from the spec template.
2. The `spec-planner` skill turns one spec into a grounded plan, including a UI section and visual
   acceptance criteria for user-facing work. It plans only — it never edits source code,
   `architecture.md` or `design.md`, and it defers architectural decisions to `adr-writer`.
3. `adr-writer` records a new decision as a proposed ADR; `accept-adr` is the only path that marks an
   ADR accepted and writes the decision into this document.
4. The `spec-implementer` agent implements a single spec, and only when its `status` is `planned`.
   Steps marked `[ui]` follow the `frontend-design` skill and `docs/design.md`.
5. `pull-request` prepares and publishes the change behind explicit approval gates.

Spec status advances through `backlog` → `ready` → `planned` → `in-progress` → `done`.

### Design principles

- **One spec, one task.** The framework targets middle-range projects implemented a single task at a
  time, not throwaway MVPs or large multi-stream efforts.
- **Narrow roles and hard gates.** Planning, deciding, implementing, and publishing are separated;
  status gates, an open-questions gate, and evidence-gated acceptance criteria prevent scope creep
  and guessing.
- **Minimal scope, never minimal finish.** Logic and backend steps get the smallest working
  solution (no speculative abstractions). UI steps follow the design rules and include the
  always-allowed polish defined in the `frontend-design` skill; nothing beyond it.
- **Specs are the source of truth.** A spec's human-written `Description` is preserved verbatim;
  anything out of scope requires updating the spec first.

### Platform dependencies

- **GitHub Copilot in VS Code (agent mode)** consumes everything under `.github/`. The framework's
  agents, skills, and prompts use Copilot's formats and are not portable to other assistants as-is.
- **Obsidian** is the human surface for `docs/`. The `board.base` kanban requires the **Bases** core
  plugin, which needs a recent Obsidian version. Per-machine Obsidian state under `docs/.obsidian/`
  is gitignored, so each user applies the recommended settings locally (see the README).
