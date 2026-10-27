# Architecture

This document describes the current, binding architecture. It is maintained only through the
[`accept-adr`](../.github/prompts/accept-adr.prompt.md) prompt, except for the foundational entry
below, which describes the SpecPilot framework itself.

## The SpecPilot framework

SpecPilot is a spec-driven development framework, not an application. It has two parts:

- **`.github/` — the automation surface.** GitHub Copilot configuration that is loaded on demand:
  `copilot-instructions.md` (always-on, deliberately brief), the `spec-planner` agent, the
  `adr-writer` and `spec-implementer` skills, the `accept-adr` and `pull-request` prompts, and the
  `docs/**` instructions. These encode the roles and gates of the workflow.
- **`docs/` — the human workspace.** An Obsidian vault holding feature specs (`docs/specs/`),
  Architecture Decision Records (`docs/adr/`), this architecture document, templates
  (`docs/_templates/`), and a `board.base` kanban view of specs by status.

### Workflow and roles

Work flows through fixed stages, each owned by one role with a narrow boundary:

1. A human writes a spec's `Description` from the spec template.
2. `spec-planner` turns one spec into a grounded plan. It plans only — it never edits source code or
   `architecture.md`, and it defers architectural decisions to `adr-writer`.
3. `adr-writer` records a new decision as a proposed ADR; `accept-adr` is the only path that marks an
   ADR accepted and writes the decision into this document.
4. `spec-implementer` implements a single spec, and only when its `status` is `planned`.
5. `pull-request` prepares and publishes the change behind explicit approval gates.

Spec status advances through `backlog` → `ready` → `planned` → `in-progress` → `done`.

### Design principles

- **One spec, one task.** The framework targets middle-range projects implemented a single task at a
  time, not throwaway MVPs or large multi-stream efforts.
- **Narrow roles and hard gates.** Planning, deciding, implementing, and publishing are separated;
  status gates, an open-questions gate, and evidence-gated acceptance criteria prevent scope creep
  and guessing.
- **Specs are the source of truth.** A spec's human-written `Description` is preserved verbatim;
  anything out of scope requires updating the spec first.

### Platform dependencies

- **GitHub Copilot in VS Code (agent mode)** consumes everything under `.github/`. The framework's
  agents, skills, and prompts use Copilot's formats and are not portable to other assistants as-is.
- **Obsidian** is the human surface for `docs/`. The `board.base` kanban requires the **Bases** core
  plugin, which needs a recent Obsidian version. Per-machine Obsidian state under `docs/.obsidian/`
  is gitignored, so each user applies the recommended settings locally (see the README).
