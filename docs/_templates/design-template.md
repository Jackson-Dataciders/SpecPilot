# Design rules

<!--
Binding design rules for UI work, read by the spec-planner and frontend-design skills.
Fill in Product and Color, keep or adjust the default rules, and add a rule when a spec needs one.
Every rule must be checkable; drop rules that are only a mood. Use the units and terms of your stack.
-->

## Product

- Character: <!-- three to five words, e.g. "calm, focused, technical" -->
- Targets: <!-- devices, screen or window sizes, and input methods the UI must work on -->

## Color

- Modes: <!-- light, dark, or both; default mode -->
- Accent: <!-- the main brand color, used for primary actions, links and focus -->
- Neutrals: <!-- base for backgrounds, surfaces, borders and text -->
- Status: <!-- success, warning and danger colors -->

## Rules

- **Colors:** only through theme tokens or resources, never raw values; text and background pairs meet WCAG AA contrast in every mode.
- **Space:** each screen uses the space its targets give it; content does not sit in a narrow strip on large screens.
- **Hierarchy:** one clear title and at most one primary action per view.
- **Grouping:** one spacing scale; the gap between groups is larger than the gap inside them.
- **Text:** secondary or small text only for supporting information, never for the main content.
