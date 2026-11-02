---
name: frontend-design
description: 'Build or change user-facing UI following the design rules in docs/design.md, with always-allowed polish and a visual review. Also sets up docs/design.md from default rules when it is missing. Use for any spec step marked [ui] or any change to what users see.'
argument-hint: 'Spec path and the UI step to build, or "setup" to create docs/design.md'
---

# Frontend Design

Build UI that is consistent, clearly structured and finished. Scope stays as small as the spec says; finish does not. Where `docs/design.md` and this skill disagree, `docs/design.md` wins.

## Design rules

`docs/design.md` is the project's binding list of design rules.

- If it is missing, set it up before any UI work: copy `docs/_templates/design-template.md`, fill in Product and Color, propose which default rules to keep or adjust, and ask the user to approve.
- Add a rule only when the spec's UI section names it. Changing or removing a rule needs its own spec.
- Every rule must be checkable.

## Always-allowed polish

In scope for every UI step, even if the spec does not mention it. A rule in `docs/design.md` may add to or narrow this list.

- Empty, loading and error states for anything that lists or loads data. An empty state says what is missing and what to do next.
- Hover, focus, pressed and disabled states on interactive elements.
- Keyboard operation and accessible names.
- Layout that holds up at every target in `docs/design.md`, including long text, names and IDs.

Not allowed without the spec asking: new features, screens, data, settings, or dependencies.

## Procedure

1. Read the spec's UI section, its visual acceptance criteria, and `docs/design.md`. Reuse existing components and screens before creating new ones.
2. Decide the visual hierarchy before building: the title, the primary action, and how secondary information is grouped.
3. Build within the design rules. Where no rule covers a choice, match the nearest existing screen instead of inventing new sizes, spacing or colors.
4. Add the always-allowed polish that applies.
5. Review the result at the targets in `docs/design.md`, using whatever the project has: screenshots, UI tests, or a manual check by the user. Check that the main content and action are recognizable at a glance, the space is used, related content is grouped, it matches similar screens, and every state looks intentional. Fix and review again.
6. Report what was built, how it was reviewed, and anything you could not verify.
