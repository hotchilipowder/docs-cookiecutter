# Development docs for {{ cookiecutter.docs_name }}

This link can be found [ {{ cookiecutter.author_name }}.github.io/{{ cookiecutter.project_name }} ](https://{{ cookiecutter.author_name }}.github.io/{{ cookiecutter.project_name }}/)

## How to contribute


## Development


### Install

```bash
uv sync
```

### Develop in localhost

```bash
bash run_dev.sh
```

### Build once

```bash
uv run sphinx-build -b html . _build
```


