# {{ cookiecutter.project_name }} Docs

{{ cookiecutter.description }}

Live site (if enabled): https://{{ cookiecutter.author_name }}.github.io/{{ cookiecutter.project_name }}/


## Development


### Install

```bash
uv sync
```

### Local preview
```bash
bash run_dev.sh
```

### Build once

```bash
uv run sphinx-build -b html . _build
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
