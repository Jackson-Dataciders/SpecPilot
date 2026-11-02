---
name: spec-planner
description: 'Turn one feature spec into a codebase-grounded implementation plan, including a UI section for user-facing work. Plans only and never implements. Use when asked to plan a spec or when a spec has status ready.'
argument-hint: 'Path to a spec file'
---

# Spec Planner

Turn one feature spec into a grounded implementation plan. The input is a path to a spec file.

## Boundaries

- Plan only. Never implement features, change application source code, or run implementation tasks, even when the current agent has the tools to do so.
- Edit files only under `docs/specs/` and `docs/adr/`. Read `docs/architecture.md`, `docs/design.md` and relevant source code, but never edit them.
- Preserve unrelated content and existing decisions. Do not guess when the spec is ambiguous.
- Use the `adr-writer` skill when a new architectural decision is required.

## Procedure

1. Read the input spec's frontmatter and Description first. Identify its affected behavior and likely code paths.
2. Read `docs/architecture.md` and the source code the feature touches. Follow the behavior to the code that directly controls it.
3. Only if the plan introduces or changes an architectural decision, list `docs/adr/` and read the ADRs with related titles. Do not re-propose alternatives rejected by those ADRs.
4. If the spec changes anything a user sees, read `docs/design.md`. If it is missing, add an Open question asking for the design rules to be set up first (`frontend-design` with `setup`).
5. If ambiguity or missing information prevents a sound plan, add the blocking items under Open questions, set frontmatter `status` to `ready`, and stop. Do not fill the plan sections in this case.
6. Otherwise, fill Behavior, UI, Out of scope, Acceptance criteria, Implementation plan, and Technical notes using the Description and inspected code. Keep criteria checkable, identify affected files/components in Technical notes, and link relevant ADRs.
7. Fill the UI section only for user-facing work; otherwise remove it. Name the screens and their states (including empty, loading and error), plus any new design rule the spec needs that `docs/design.md` lacks. Add visual acceptance criteria that can be checked at the targets in `docs/design.md`. Mark plan steps that build UI with a leading `[ui]` so the implementer applies the `frontend-design` skill to them.
8. If a new architectural decision is needed, create its ADR using the `adr-writer` skill, save it under `docs/adr/`, and add its path to the spec's `adr` frontmatter property. Do not edit `docs/architecture.md`.
9. Remove Open questions if none remain, set frontmatter `status` to `planned`, and give a concise plan summary followed by exactly `Spec: <path>` using the input spec path. Tell the user to run the `spec-implementer` agent on it; never start implementing yourself.
