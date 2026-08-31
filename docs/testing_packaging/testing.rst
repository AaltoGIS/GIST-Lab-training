Testing a Python library
========================

A **test** is a small piece of code that checks whether your package behaves as
expected. When we write tests, we turn our expectations into executable checks:
this function should return a ``GeoDataFrame``; this invalid file should raise a
clear error; this optional dependency should be handled gracefully.

In a library project, tests usually live in a folder called ``tests/``. Pyrosm
follows this convention with files such as ``tests/test_main.py``,
``tests/test_data.py``, and ``tests/test_graph_exports.py``. The file names
begin with ``test_`` so that `pytest <https://docs.pytest.org/>`__, the testing
tool used by pyrosm, can find them automatically.

Core testing terms
------------------

A **test case** is one individual check. In ``pytest``, it is usually a function
whose name starts with ``test_``:

.. code-block:: python

   def test_network(test_pbf):
       from pyrosm import OSM
       from geopandas import GeoDataFrame

       osm = OSM(test_pbf)
       gdf = osm.get_network()
       assert isinstance(gdf, GeoDataFrame)

Notice the shape of the test. It prepares an ``OSM`` object, calls
``get_network()``, and then uses an **assertion** to check the result. An
assertion is a statement that must be true. If it is false, the test fails.

A **fixture** is reusable setup code for tests. Pyrosm uses fixtures to provide
small test files:

.. code-block:: python

   @pytest.fixture
   def test_pbf():
       pbf_path = get_data("test_pbf")
       return pbf_path

With this fixture, any test can ask for ``test_pbf`` as an argument. Pytest then
runs the fixture and passes the returned file path into the test. This keeps the
test itself short and focused.

What pyrosm tests
-----------------

Pyrosm tests several kinds of behaviour:

- **Basic public API behaviour**: can users import ``pyrosm.OSM`` and call the
  main methods?
- **Return types**: do functions return the expected object type, such as a
  ``GeoDataFrame``?
- **Error handling**: does invalid input raise a meaningful exception instead of
  a cryptic low-level error?
- **Regression fixes**: does a previously fixed bug stay fixed?
- **Optional dependencies**: do graph exports work with backends such as
  ``networkx``, ``igraph``, ``pandana``, and ``pandarm`` when they are installed?
- **Platform differences**: do tests behave correctly on Linux, macOS, and
  Windows?

This is a useful model for a beginner package. You do not need hundreds of
tests on day one. Start with tests that cover the main user-facing behaviour,
then add a regression test whenever you fix a bug.

Testing errors
--------------

Good tests do not only check successful cases. They also check that wrong input
fails in a helpful way. Pyrosm has tests where invalid ``.pbf`` files should
raise ``InvalidOSMFileError``:

.. code-block:: python

   with pytest.raises(InvalidOSMFileError):
       OSM(short)

Here ``pytest.raises()`` means: this block is expected to raise this exception.
If no exception is raised, or if the wrong exception is raised, the test fails.

Testing with external services
------------------------------

Some tests are fragile because they depend on the internet, a database, or an
external service. Pyrosm needs to test downloads from OpenStreetMap data
providers, but it avoids running those live download tests on every operating
system and Python version. Instead, the test suite uses a ``RUN_DOWNLOAD_TESTS``
environment variable and ``pytest.mark.skipif`` to run them only in one selected
CI job.

The lesson is simple: keep most tests fast, local, and repeatable. If you need
live-service tests, mark them clearly and run them in a controlled way.

For more practical advice on designing a test suite, see :doc:`good_practices`.

Coverage
--------

**Coverage** measures which parts of your code were executed during the test
run. Pyrosm uses ``pytest-cov`` and uploads coverage information to Codecov from
GitHub Actions. Coverage is useful because it shows which modules or branches
have no tests.

Coverage is not a quality score by itself. A test can execute a line without
checking the important behaviour. Use coverage as a map: it helps you find
untested areas, but you still need meaningful assertions.

Running tests locally
---------------------

In a simple package, you can often run tests with:

.. code-block:: bash

   pytest -v

Pyrosm has compiled Cython extensions and geospatial dependencies, so its local
development setup is more involved. The README recommends creating a Conda
environment from one of the files under ``ci/`` and then installing the package
in editable mode:

.. code-block:: bash

   micromamba create -f ci/314-conda.yaml
   micromamba activate test
   pip install -e . --no-build-isolation
   pytest -v

For your own beginner package, the same idea applies even if the commands are
shorter: create an environment, install the package, and run the tests before
opening a pull request.
