Continuous integration with GitHub Actions
==========================================

**Continuous integration** means that tests run automatically whenever the code
changes. In a GitHub project, this usually means running tests on every pull
request and on pushes to the main branch.

GitHub Actions is GitHub's built-in automation system. A workflow is a YAML file
under ``.github/workflows/``. Pyrosm uses workflows for tests and releases:

- ``.github/workflows/tests.yaml`` runs linting, tests, coverage, and a separate
  acceptance job for ``r5py``.
- ``.github/workflows/release.yaml`` reuses the test workflow, builds release
  artefacts, publishes to PyPI, and creates a GitHub release.

The basic vocabulary
--------------------

A **workflow** is one automation file. A **job** is a group of steps that runs on
a virtual machine. A **step** is one action or shell command. A **runner** is the
machine where the job runs, such as ``ubuntu-latest`` or ``windows-latest``.

A **matrix** repeats the same job with different settings. Pyrosm uses a matrix
to run tests across operating systems and Python versions:

.. code-block:: yaml

   strategy:
     fail-fast: false
     matrix:
       os:
         - ubuntu-latest
         - windows-latest
         - macos-latest
       env:
         - ci/310-conda.yaml
         - ci/311-conda.yaml
         - ci/312-conda.yaml
         - ci/313-conda.yaml
         - ci/314-conda.yaml

This creates many test jobs: each operating system is combined with each
environment file. That is how pyrosm checks Python 3.10-3.14 on Linux, Windows,
and macOS.

The pyrosm test workflow
------------------------

The pyrosm test workflow has three main jobs:

- ``lint`` checks code formatting and style with ``black`` and ``flake8``.
- ``test`` installs a Conda environment with Micromamba, installs pyrosm in
  editable mode, and runs ``pytest`` with coverage.
- ``r5py`` runs a heavier acceptance test separately because ``r5py`` depends on
  the Java Virtual Machine and is not part of the main test matrix.

The workflow uses ``needs: lint`` so that the test jobs wait for linting to
finish. This keeps the workflow organised: first check style, then run the more
expensive tests.

A small CI workflow for a beginner package
------------------------------------------

Your first workflow can be much smaller than pyrosm's. For a pure-Python
package, a useful starting point is:

.. code-block:: yaml

   name: tests

   on:
     push:
       branches: [main]
     pull_request:

   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v5
         - uses: actions/setup-python@v6
           with:
             python-version: "3.12"
         - run: python -m pip install --upgrade pip
         - run: python -m pip install -e ".[test]"
         - run: pytest -v

This workflow checks out the code, installs Python, installs your package with
its test dependencies, and runs ``pytest``. Once this is working, you can add a
matrix for multiple Python versions or operating systems.

Linting
-------

**Linting** checks code style and common mistakes. Pyrosm runs:

.. code-block:: bash

   python -m black --check pyrosm
   python -m flake8 pyrosm

``black --check`` verifies that files are already formatted. It does not rewrite
them in CI. If the check fails, the developer formats the code locally and
pushes the fix.

Skipping expensive or fragile tests
-----------------------------------

Pyrosm does not run every live download test in every matrix job. The workflow
sets ``RUN_DOWNLOAD_TESTS`` to ``true`` for one selected runner, and the tests
use ``pytest.mark.skipif`` elsewhere. This avoids unnecessary load on external
services and makes the test suite less fragile.

This is a good pattern for your own package:

- Run fast unit tests everywhere.
- Run integration tests in fewer jobs.
- Avoid hitting external services in every pull request unless you really need
  to.

Release workflows
-----------------

The pyrosm release workflow starts when a Git tag beginning with ``v`` is
pushed. It first calls the test workflow:

.. code-block:: yaml

   jobs:
     tests:
       name: Tests
       uses: ./.github/workflows/tests.yaml
       secrets: inherit

This is a useful design. A release should only happen after the same tests that
protect pull requests have passed. The workflow then builds wheels and an sdist,
publishes them to PyPI, and creates a GitHub release.

For a beginner project, you can first run release workflows manually with
``workflow_dispatch``. Once the process is reliable, you can publish from tags.
