# AGENTS Guide for {{ cookiecutter.project_name }} Docs

This file defines how coding agents should work in a generated docs workspace.

## Scope
- Primary scope: the `{{ cookiecutter.docs_name }}/` directory.
- Secondary scope: related CI docs workflow under `.github/workflows/` when docs deploy is involved.
- Avoid unrelated app/business logic changes unless explicitly requested.

## Context
- This file is for the generated project docs workspace.
- If you are editing the cookiecutter template itself, follow the repository root `AGENTS.md` instead.

## Goals
- Keep documentation accurate, buildable, and easy to navigate.
- Prefer small, reviewable edits with clear rationale.
- Keep examples runnable and commands copy-paste safe.

## Working Protocol
1. Read this file, then `readme.md`, then `index.rst`.
2. For structural changes, update navigation in `index.rst`.
3. For environment/dependency changes, update both docs and requirements files.
4. Validate locally before finishing.

## Documentation Rules
- Use concise Chinese or English consistently per page; do not mix styles in one paragraph.
- Keep one topic per page; split long pages into focused files.
- Add practical commands first, explanations second.
- Prefer Markdown for content pages; keep `index.rst` as toctree entry point.

## Commands Agents Should Use
- Install:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
- Live preview:
```bash
bash run_dev.sh
```
- Build check:
```bash
sphinx-build -b html . _build/html
```

## Definition of Done
- Docs build succeeds with no new warnings introduced by this change.
- `index.rst` navigation includes any newly added page.
- Commands in changed docs are syntactically valid.
- If deployment behavior changes, update workflow docs in `readme.md`.

## Safe Change Boundaries
- Do not delete large sections without replacing intent.
- Do not change CI workflow triggers/permissions silently.
- Do not introduce new tooling unless the request requires it.

## Suggested Deliverable Format
- Brief change summary.
- Files changed and why.
- Validation commands run and outcomes.
- Follow-up items, if any.
