# docs-cookiecutter
<<<<<<< HEAD
Fast Sphinx docs template with Markdown support.

## Create a project

```bash
uvx cookiecutter https://github.com/hotchilipowder/docs-cookiecutter.git
```

## Local development (template repo)

```bash
cd docs
uv sync
uv run sphinx-build -b html . _build
```

## Smoke test this template

```bash
bash scripts/smoke_test_template.sh
```

## GitHub Pages notes

1. Open `Settings -> Pages` and select `gh-pages`.
2. If you see `Permission to xxx/xxxx.git denied to github-actions[bot]`, set `Settings -> Actions -> General -> Workflow permissions`.
3. If `main` cannot deploy because of environment protection rules, update `Settings -> Environments`.
=======
Fast Sphinx docs template with Markdown (MyST) support, GitHub Pages deploy, and batteries-included extensions.

## What you get
- Sphinx + MyST + common extensions (mermaid, design, copybutton, emoji, bibtex)
- One-command local preview
- Optional GitHub Actions deploy to GitHub Pages
- Clean project structure ready for content

## Quick start
```bash
pipx install cookiecutter
cookiecutter https://github.com/hotchilipowder/docs-cookiecutter.git
```

You will be prompted for:
- `project_name` (used for docs title and repo)
- `docs_name` (docs directory name, default `docs`)
- `author_name`
- `description`
- `include_github_actions` (yes/no)

## Generated structure
```
<project>
  <docs_name>/
    conf.py
    index.rst
    readme.md
    requirements.txt
    run_dev.sh
    github_actions/ (optional)
```

## GitHub Pages deployment
If you enabled `include_github_actions`, a workflow is created under `<docs_name>/github_actions/build-docs.yml`.

Common fixes:
- Enable Pages: Settings -> Pages -> Branch -> `gh-pages`
- Workflow permissions: Settings -> Actions -> General -> allow `GITHUB_TOKEN` write
- If main is protected by environment rules: Settings -> Environments -> adjust `github-pages`

## Notes
- The workflow uses `<docs_name>` for the docs path. If you change `docs_name`, it will stay consistent.
>>>>>>> b967561 (updated)

