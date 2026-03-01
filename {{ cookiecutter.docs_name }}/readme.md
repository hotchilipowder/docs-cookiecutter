# {{ cookiecutter.project_name }} Docs

{{ cookiecutter.description }}

Live site (if enabled): https://{{ cookiecutter.author_name }}.github.io/{{ cookiecutter.project_name }}/

<<<<<<< HEAD

## Development


### Install

```bash
uv sync
=======
## Contents
- `index.rst`: entry page
- `conf.py`: Sphinx config
- `_static/`, `_templates/`: assets and overrides
- `refs.bib`: bibliography (if used)

## Quick start
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
>>>>>>> b967561 (updated)
```

### Local preview
```bash
bash run_dev.sh
```

<<<<<<< HEAD
### Build once

```bash
uv run sphinx-build -b html . _build
=======
### Build HTML
```bash
sphinx-build -b html . _build/html
>>>>>>> b967561 (updated)
```

## Writing docs
- Use Markdown (`.md`) or reStructuredText (`.rst`)
- Add new pages and link them from `index.rst`
- Mermaid diagrams are supported via fenced blocks

## Contributing
1. Create a branch
2. Update docs content
3. Build locally and verify
4. Open a PR

## Troubleshooting
- If Pages doesn’t deploy, check workflow permissions and environment rules

