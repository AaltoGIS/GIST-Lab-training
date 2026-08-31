Packaging a Python library
==========================

**Packaging** means preparing your code so that other people can install it with
tools such as ``pip``. A Python package needs more than source code: it needs
metadata, dependencies, build instructions, and release artefacts.

Pyrosm is a useful example because it is a real package on PyPI, and because it
contains compiled Cython modules. Most beginner packages are simpler, but the
same concepts still apply.

The main packaging files
------------------------

Pyrosm uses three important packaging files:

- ``setup.py`` defines package metadata, dependencies, supported Python
  versions, and the Cython extension build.
- ``pyproject.toml`` defines the build-system requirements and ``cibuildwheel``
  settings.
- ``MANIFEST.in`` tells the source distribution which extra files and folders to
  include.

In modern Python packaging, many projects put most metadata directly in
``pyproject.toml``. Pyrosm still keeps much of it in ``setup.py`` because it has
a more complex compiled build. For a new pure-Python package, it is usually
reasonable to start with ``pyproject.toml`` only.

Metadata
--------

**Metadata** tells package indexes and installers what your package is. In
pyrosm, this includes the package name, version, license, author, description,
project URLs, keywords, supported Python versions, and dependencies.

A simplified example looks like this:

.. code-block:: python

   setup(
       name="pyrosm",
       version="0.10.0rc1",
       license="MIT",
       description="A Python tool to parse OSM data from Protobuf format into GeoDataFrame.",
       python_requires=">=3.10",
       install_requires=[
           "geopandas>=0.12.0",
           "shapely>=2.1",
           "protobuf>=6.33.5",
       ],
   )

The important beginner lesson is that dependencies should be declared in the
package metadata. If your package imports ``geopandas``, users should not have
to discover that manually after installation fails.

Source distributions and wheels
-------------------------------

Python packages are commonly distributed in two formats:

- A **source distribution** or **sdist** is an archive of the source files needed
  to build the package.
- A **wheel** is a built package that ``pip`` can install directly.

For a pure-Python package, one wheel can often work on all operating systems.
For a package with compiled extensions, such as pyrosm, wheels are platform
specific. This is why pyrosm uses ``cibuildwheel``: it builds wheels for several
Python versions and operating systems.

Build isolation
---------------

When ``pip`` builds a package, it normally creates an isolated build
environment. The build dependencies come from ``pyproject.toml``:

.. code-block:: toml

   [build-system]
   requires = ["setuptools", "wheel", "Cython", "cykhash>=2"]

For pyrosm development, the README uses ``pip install -e . --no-build-isolation``
inside a prepared Conda environment. This tells ``pip`` to use the build
dependencies already installed in that environment. That is useful for pyrosm
because Cython and geospatial dependencies are easier to control through
Conda-forge.

For a beginner pure-Python library, you usually do not need
``--no-build-isolation``.

Including the right files
-------------------------

``MANIFEST.in`` matters when building an sdist. Pyrosm includes its package
files, CI files, protocol buffer definitions, tests, and ``pyproject.toml``:

.. code-block:: text

   graft pyrosm
   graft ci
   graft proto
   graft tests
   include pyproject.toml
   global-exclude __pycache__/*

This helps ensure that someone can build the package from the source archive.
If your package needs data files, schemas, templates, or generated sources, you
need to make sure they are included in the distribution.

Publishing to PyPI
------------------

**PyPI** is the main package index for Python. When users run ``pip install
pyrosm``, ``pip`` downloads the package from PyPI.

Pyrosm publishes through GitHub Actions. When a version tag such as ``v0.10.0``
is pushed, the release workflow:

1. Runs the test workflow.
2. Checks that the Git tag matches the package version.
3. Builds wheels on Linux, Windows, and macOS with ``cibuildwheel``.
4. Builds an sdist with ``python -m build`` through ``pipx run build --sdist``.
5. Uploads the release artefacts to PyPI.
6. Creates a GitHub release.

The PyPI publish step uses **Trusted Publishing**. This means the workflow uses
OpenID Connect (OIDC) instead of a long-lived PyPI API token stored as a GitHub
secret. For new projects, Trusted Publishing is a good default when you are
ready to automate releases.

A beginner release checklist
----------------------------

Before publishing your own package, check that:

- The package installs in a clean environment.
- The tests pass locally.
- The version number has been updated.
- The README explains installation and basic use.
- ``python -m build`` creates both an sdist and a wheel.
- You have tested the built wheel, not only the source checkout.
- The GitHub Actions test workflow is green.

For a first release, it is often useful to publish to TestPyPI before publishing
to the real PyPI project.
