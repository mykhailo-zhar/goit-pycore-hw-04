# goit-pycore-hw-04

GoIT **Python Core** homework: small file-driven utilities, CLI helpers, and tests.

## Tasks and results

**Task 1 — Salary totals**  
Reads a comma-separated file of employee name and salary, validates lines, and computes **total** and **average** salary ([`src/salary.py`](src/salary.py), shared rules in [`src/validations.py`](src/validations.py)). Demos run from [`main.py`](main.py) via `salary_demo`.

**Task 2 — Cat records**  
Parses lines `id,name,age`, validates fields, and returns a **list of dicts** with string values ([`src/cats.py`](src/cats.py)). Demos run from `main.py` via `cats_demo`.

**Directory tree (CLI)**  
Script under [`src/scripts/display_directory_tree.py`](src/scripts/display_directory_tree.py): prints a root directory with colorized names, **directories before files**, two levels of detail, and **item counts** for deeper folders (`colorama`). Accepts the path as the first CLI argument.

**Contacts assistant (CLI)**  
Interactive-style bot in [`src/scripts/contacts_bot.py`](src/scripts/contacts_bot.py): `parse_input()`, `add_contact`, `change_contact` (user command `update`), `show_phone`, `show_all`, and a **`main()`** loop; contacts live in a dict (name → phone) with validation for alphanumeric names and any kind digit phones.

## Tests and docs

- **Tests**: `pytest` under [`tests/`](tests/) (salary, cats, directory tree, contacts bot).
- **API docs**: Sphinx—generate stubs with `mise run gd` (or `sphinx-apidoc`), build HTML with `mise run bd`; output in `docs/build/`.

## Quick commands

```bash
uv sync
pytest
python main.py
```

Use `uv run` or an activated `.venv` if your shell is not already using the project environment.
