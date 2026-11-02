# Contributing

Anyone with access is welcome to contribute, and anyone may use SpecPilot (see the [LICENSE](LICENSE)).

## How to contribute

1. Read the [README](README.md) and [`docs/architecture.md`](docs/architecture.md) to understand the workflow.
2. Follow the conventions in [`.github/instructions/docs.instructions.md`](.github/instructions/docs.instructions.md) for anything under `docs/` (naming, status values, dates, relative links).
3. Use the framework on itself where it fits: write a spec, plan it, and implement one task at a time.
4. Run the docs lint before opening a PR:
   ```bash
   python scripts/lint_docs.py
   ```
5. Open a pull request (the `pull-request` prompt can prepare one). Keep changes focused and describe what changed and why.
