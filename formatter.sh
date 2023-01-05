#!/bin/sh
#
# Run fmt for `campaigns-backend`.
# format = write formatting updates

# Format.
isort . --skip __init__.py
black . --line-length 120

# Generate directory tree.
tree -a -I '.git|.vscode|__pycache__|run' > dir.tree
pipenv graph > graph.txt
