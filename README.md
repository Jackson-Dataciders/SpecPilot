# SpecPilot

A lightweight Copilot framework for spec driven development.

You write *what* a feature should do in plain words. Copilot turns it into a plan, records architectural decisions, implements it, and opens the PR. Obsidian is the human-facing workspace for specs and ADRs.

## How it works

1. **Write a spec.** Create a note from the spec template and fill in only the `Description`.
2. **Plan.** Run the `spec-planner` agent on the spec. It fills in behavior, scope, acceptance criteria and the implementation plan, and creates an ADR if a new architectural decision is needed. Answer any `Open questions`.
3. **Accept decisions.** Review proposed ADRs, then run the `accept-adr` prompt to record them in `docs/architecture.md`.
4. **Implement.** Use the `Implement spec` handoff (or the `spec-implementer` skill) on a spec with status `planned`.
5. **Publish.** Run the `pull-request` prompt. It asks for approval before committing, pushing and creating the PR.

Spec status moves through `backlog` → `ready` → `planned` → `in-progress` → `done`.

## Repository layout

| Path | Purpose |
| --- | --- |
| `docs/` | The Obsidian vault |
| `docs/specs/` | Feature specs (`NNN-kebab-title.md`) and the `board.base` kanban |
| `docs/adr/` | Architecture Decision Records (`NNNN-kebab-title.md`) |
| `docs/_templates/` | Spec and ADR templates |
| `docs/architecture.md` | Current, binding architecture |
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

Use GitHub Copilot in VS Code with agent mode, with the repository open at its root so `.github/` is picked up. Select the `spec-planner` agent and give it the spec path.

## Ground rules

- `docs/architecture.md` is binding and only changes through the `accept-adr` prompt.
- Never edit a spec's `Description` after writing it; Copilot must preserve it verbatim.
- Use relative Markdown links, never wikilinks.
- Specs are the source of truth. If implementation needs something out of scope, update the spec first.
