# AGENTS Guide for docs-cookiecutter

This repository is a Cookiecutter template, not a runtime docs project.

## Tool Purpose
- Generate a Sphinx documentation workspace quickly.
- Support Markdown (MyST), local preview, and optional GitHub Pages deploy workflow.
- Provide a reusable docs skeleton under `{{ cookiecutter.docs_name }}/`.

## Inputs (Cookiecutter Variables)
- `project_name`: project/docs title and repo name reference.
- `docs_name`: generated docs directory name (default `docs`).
- `author_name`: author and GitHub Pages URL parts.
- `description`: short project description.
- `include_github_actions`: whether to include docs deploy workflow.

## Outputs (Generated Project)
- A docs workspace at `<docs_name>/` with:
  - `conf.py`, `index.rst`, `readme.md`
  - `requirements.txt`, `requirements-dev.txt`, `run_dev.sh`
  - `AGENTS.md` for downstream coding agents
- If enabled, workflow template `github_actions/build-docs.yml` is copied to `.github/workflows/` by hook.

## How Agents Should Work Here
1. Treat this repo as a template source.
2. Edit template files under `{{ cookiecutter.docs_name }}/` when changing generated behavior.
3. Edit `hooks/` only when generation/copy behavior must change.
4. Keep variable placeholders intact (`{{ cookiecutter.* }}`) unless intentionally replacing template behavior.

## Boundaries
- Do not replace template placeholders with fixed values accidentally.
- Do not move files referenced by hooks unless hooks are updated in the same change.
- Do not introduce docs commands that conflict with existing `run_dev.sh` and requirements flow.

## Validation Checklist
- Template placeholders are still renderable.
- Generated docs flow remains: install -> preview -> build.
- GitHub Actions template still resolves docs path via `{{ cookiecutter.docs_name }}`.
- README instructions match current template behavior.
