#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d /tmp/docs-cookiecutter-smoke.XXXXXX)"
PROJECT_NAME="smoke-docs"

echo "[smoke] temp dir: ${TMP_DIR}"
echo "[smoke] generating project from template..."
uvx cookiecutter "${ROOT_DIR}" --no-input --output-dir "${TMP_DIR}" project_name="${PROJECT_NAME}"

DOCS_DIR="$(dirname "$(find "${TMP_DIR}" -maxdepth 3 -type f -name conf.py -print -quit)")"
if [[ -z "${DOCS_DIR}" || ! -d "${DOCS_DIR}" ]]; then
  echo "[smoke] failed to locate generated docs directory" >&2
  exit 1
fi
echo "[smoke] docs dir: ${DOCS_DIR}"

echo "[smoke] syncing dependencies..."
uv sync --directory "${DOCS_DIR}"

echo "[smoke] building docs..."
uv run --directory "${DOCS_DIR}" sphinx-build -b html . _build

echo "[smoke] success"
