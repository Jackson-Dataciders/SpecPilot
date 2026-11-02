# SpecPilot

A lightweight Copilot framework for spec driven development.

You write *what* a feature should do in plain words. Copilot turns it into a plan, records architectural decisions, implements it, and opens the PR. Obsidian is the human-facing workspace for specs and ADRs.

## Requirements

- **GitHub Copilot in VS Code** (agent mode). The `.github/` agents, prompts and skills use Copilot's formats and are not portable to other assistants as-is.
- **Obsidian** for the `docs/` vault. The `board.base` kanban needs the **Bases** core plugin, so use a recent Obsidian version.
- **Python 3** only if you want to run the docs lint (`scripts/lint_docs.py`); the workflow runs it in CI.

## How it works

1. **Write a spec.** Create a note from the spec template and fill in only the `Description`.
2. **Plan.** Ask Copilot to plan the spec; it uses the `spec-planner` skill. It fills in behavior, UI, scope, acceptance criteria and the implementation plan, and creates an ADR if a new architectural decision is needed. Answer any `Open questions`.
3. **Accept decisions.** Review proposed ADRs, then run the `accept-adr` prompt to record them in `docs/architecture.md`.
4. **Implement.** Select the `spec-implementer` agent and give it a spec with status `planned`. Logic and backend steps get the smallest working solution; UI steps follow the `frontend-design` skill and `docs/design.md`.
5. **Publish.** Run the `pull-request` prompt yourself. It asks for approval before committing, pushing and creating the PR.

Before the first UI spec, set up the design rules: ask Copilot to run the `frontend-design` skill with `setup`. It creates `docs/design.md` from pre-written default rules, adjusts them to your product and asks you to approve. Add rules later as specs need them.

### Quality bar

Scope is always minimal: build only what the spec asks for. Finish is not: UI work meets `docs/design.md` and includes the always-allowed polish (empty, loading and error states, interaction states, keyboard and accessibility, layout at every target) listed in the `frontend-design` skill.

Spec status moves through `backlog` → `ready` → `planned` → `in-progress` → `done`.

## Repository layout

| Path | Purpose |
| --- | --- |
| `docs/` | The Obsidian vault |
| `docs/specs/` | Feature specs (`NNN-kebab-title.md`) and the `board.base` kanban |
| `docs/adr/` | Architecture Decision Records (`NNNN-kebab-title.md`) |
| `docs/_templates/` | Spec and ADR templates |
| `docs/architecture.md` | Current, binding architecture |
| `docs/design.md` | Binding design rules for UI work (started from default rules, extended per spec) |
| `.github/` | Copilot instructions, agents, prompts and skills |

## Setup

### 1. Get the repository

Copy `.github/` and `docs/` into your project root (or clone this repo and work inside it).

### 2. Open the vault in Obsidian

1. Install [Obsidian](https://obsidian.md).
2. Choose **Open folder as vault** and select the `docs/` folder, not the repo root.
3. If prompted, trust the vault's author to enable plugins.

### 3. Recommended Obsidian settings

These are the defaults this framework assumes. Check them under **Settings**.

- **Core plugins:** enable *Templates*, *Properties*, *Bases*, *Backlinks* and *Graph view*.
- **Templates:** set the template folder to `_templates`.
- **Files and links:**
  - Turn on **Use Markdown links** and set **New link format** to *Relative path to file*. Wikilinks are not allowed in this repo.
  - Set **Default location for new notes** to the folder `specs`.
- **Template date format:** `YYYY-MM-DD` (the docs rules require it; the Obsidian default differs).

### 4. Create your first spec

1. Open the command palette and run **Templates: Insert template**, choosing `_specs-template`, in a new note inside `specs/`.
2. Name it `NNN-kebab-title.md` (for example `001-user-login.md`).
3. Write the `Description` and leave everything below the divider for Copilot.
4. Set `status: ready` when it is ready to plan.
5. Open `specs/board.base` to see all specs as a kanban board grouped by status.

### 5. Copilot

Use GitHub Copilot in VS Code with agent mode, with the repository open at its root so `.github/` is picked up. To plan, ask Copilot to plan the spec path (the `spec-planner` skill). To implement, select the `spec-implementer` agent and give it the spec path.

## Ground rules

- `docs/architecture.md` is binding and only changes through the `accept-adr` prompt.
- Never edit a spec's `Description` after writing it; Copilot must preserve it verbatim.
- Use relative Markdown links, never wikilinks.
- Specs are the source of truth. If implementation needs something out of scope, update the spec first.
