Checklist for your own package
==============================

This checklist turns the pyrosm example into a smaller workflow that suits a
beginner Python library.

Testing
-------

- Create a ``tests/`` folder.
- Install ``pytest``.
- Add one test file for each important module or user-facing feature.
- Start with tests for the main successful use cases.
- Add tests for invalid input and helpful error messages.
- Add a regression test whenever you fix a bug.
- Use small bundled sample data whenever possible.
- Keep tests fast enough that developers can run them often.
- Give tests descriptive names that explain the behaviour being checked.
- Use fixtures for repeated setup code.
- Keep most tests independent of external services.
- Separate slow integration tests from fast unit tests.
- Run ``pytest -v`` before opening a pull request.

Packaging
---------

- Put package metadata and build settings in ``pyproject.toml``.
- Declare runtime dependencies clearly.
- Add optional dependency groups for development and testing if needed.
- Check that ``pip install -e .`` works in a clean environment.
- Build the package with ``python -m build``.
- Test the built wheel in a fresh environment.
- Publish to TestPyPI before the first real PyPI release.

Continuous integration
----------------------

- Add ``.github/workflows/tests.yaml``.
- Run tests on pull requests and pushes to the main branch.
- Start with one Python version on Ubuntu.
- Add more Python versions after the first workflow is stable.
- Add Windows and macOS if your package handles file paths, compiled code,
  geospatial dependencies, or platform-specific behaviour.
- Keep slow integration tests separate from fast unit tests.

Documentation
-------------

- Explain installation in the README.
- Add a short usage example that users can run.
- Document how contributors should create an environment and run tests.
- Build documentation with Sphinx if your package has tutorials, examples, or
  an API reference.
- Keep the documentation build as lightweight as possible.

Release
-------

- Update the version number.
- Update the changelog or release notes.
- Check that tests pass locally and in CI.
- Build release artefacts.
- Publish from GitHub Actions when the process is reliable.
- Prefer PyPI Trusted Publishing over long-lived PyPI tokens.
