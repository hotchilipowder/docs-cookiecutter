# docs-cookiecutter
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

