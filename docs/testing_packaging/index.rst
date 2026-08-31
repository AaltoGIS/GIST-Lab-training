Testing and packaging Python libraries
======================================

This module introduces the basic ideas of testing, packaging, and continuous
integration for Python libraries. We use `pyrosm
<https://github.com/pyrosm/pyrosm>`__ as the running example because it is a
real open-source package with compiled code, documentation, tests, GitHub
Actions workflows, and PyPI releases.

The aim is not to copy every detail from pyrosm. Instead, we use it to learn the
vocabulary and the development workflow that your own package can grow towards.

.. image:: /_static/comic-testing.svg
   :width: 100%
   :alt: Three-panel comic. A researcher sees a significant result and sends it to the paper; a co-author examining the code finds it counts every row twice; the researcher, at a passing test, says a test would have caught that. Caption: a test catches the bug that looks right.

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

.. toctree::
    :caption: Testing
    :maxdepth: 1

    testing
    good_practices

.. toctree::
    :caption: Packaging and automation
    :maxdepth: 1

    packaging
    continuous_integration

.. toctree::
    :caption: Putting it together
    :maxdepth: 1

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
