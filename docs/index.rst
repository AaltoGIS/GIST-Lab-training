Testing and packaging Python libraries
======================================

This short module introduces the basic ideas of testing, packaging, and
continuous integration for Python libraries. We use `pyrosm
<https://github.com/pyrosm/pyrosm>`__ as the running example because it is a
real open-source package with compiled code, documentation, tests, GitHub
Actions workflows, and PyPI releases.

The aim is not to copy every detail from pyrosm. Instead, we use it to learn
the vocabulary and the development workflow that your own package can grow
towards.

Learning objectives
-------------------

At the end of this module, you should be able to:

- Explain why automated tests are useful in a Python library.
- Define common testing terms such as **test case**, **fixture**, **assertion**,
  **skip**, and **coverage**.
- Choose test data and test structure that keep the test suite fast and
  reliable.
- Recognise the main files that define how a Python package is built.
- Explain the difference between a **source distribution** and a **wheel**.
- Describe how GitHub Actions can run tests automatically on pull requests.
- Sketch a simple release workflow that builds and publishes a package to PyPI.

Contents
--------

.. toctree::
   :maxdepth: 2

   testing
   good_practices
   packaging
   continuous_integration
   checklist

Sources
-------

The examples in this module are based on the current pyrosm repository files,
especially:

- `tests/ <https://github.com/pyrosm/pyrosm/tree/master/tests>`__
- `setup.py <https://github.com/pyrosm/pyrosm/blob/master/setup.py>`__
- `pyproject.toml <https://github.com/pyrosm/pyrosm/blob/master/pyproject.toml>`__
- `MANIFEST.in <https://github.com/pyrosm/pyrosm/blob/master/MANIFEST.in>`__
- `.github/workflows/tests.yaml <https://github.com/pyrosm/pyrosm/blob/master/.github/workflows/tests.yaml>`__
- `.github/workflows/release.yaml <https://github.com/pyrosm/pyrosm/blob/master/.github/workflows/release.yaml>`__
- `docs/conf.py <https://github.com/pyrosm/pyrosm/blob/master/docs/conf.py>`__
