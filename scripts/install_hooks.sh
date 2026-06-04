#!/usr/bin/env sh
# Install pre-commit hooks for LLM Wiki maintenance.
set -e
cd "$(dirname "$0")/.."
git config core.hooksPath .githooks
echo "Installed hooks: core.hooksPath=.githooks"
echo "Pre-commit runs: wiki_tool.py build, lint, source-lint"
