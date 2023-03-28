# pycomole

[![Test](https://github.com/ziyunli/pycomole/actions/workflows/test.yml/badge.svg)](https://github.com/ziyunli/pycomole/actions/workflows/test.yml)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


---

**Documentation**: [https://ziyunli.github.io/pycomole](https://ziyunli.github.io/pycomole)

**Source Code**: [https://github.com/ziyunli/pycomole](https://github.com/ziyunli/pycomole)

---

Coding exercises in Python.

## Development

Requirements:
* [Nix: the package manager](https://nixos.org/download.html)
* [direnv](https://direnv.net/)
* [devenv](https://devenv.sh/)

### Activate the development environment

```bash
devenv shell
poetry env use python
poetry install
```

### Testing

```bash
pytest
```

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

You can run it locally via:

```sh
mkdocs serve
```

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```

---

This project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.
