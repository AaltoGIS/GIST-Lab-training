Good testing practices
======================

Good tests help you change the package without fear. They should be easy to run,
easy to understand, and focused on behaviour that matters to users. This page
summarises practical habits that are especially useful for beginner package
developers.

Keep tests fast
---------------

A fast test suite is a test suite that people actually run. If the tests take
only a few seconds or minutes, you can run them before every commit and GitHub
Actions can run them on every pull request. If the tests take too long, people
start skipping them, and bugs reach the main branch more easily.

One common reason tests become slow is that they use too much data. Pyrosm works
with OpenStreetMap extracts that can be very large, but the test suite usually
uses small sample files. For example, many tests use ``get_data("test_pbf")`` or
other small bundled extracts instead of downloading and parsing a large country
file.

For your own package, prefer the smallest input that still tests the behaviour:

- Use a tiny table instead of a large database dump.
- Use a small GeoPackage, GeoJSON, or raster tile instead of a national dataset.
- Use a few representative rows or features instead of thousands.
- Use synthetic data when the exact real-world file is not important.
- Keep live downloads out of the main test path.

Bundle small sample data
------------------------

Small **test fixtures** can live inside the repository. In a spatial package,
these might be small vector files, short CSV files, tiny rasters, or compressed
sample extracts. The key idea is that the files should be small enough to store
in Git and stable enough that test results do not change unexpectedly.

Pyrosm bundles test data that ``get_data()`` can return during tests. This makes
many tests local and repeatable: the test does not need an internet connection,
and the expected output does not change because an external provider updated a
file.

When you add bundled test data, keep a few rules in mind:

- Include only data that you are allowed to redistribute.
- Keep files as small as possible.
- Document where the sample came from and why it is included.
- Prefer one clear sample per testing purpose over one large "everything" file.
- Avoid private, sensitive, or personally identifiable data.

Test one idea at a time
-----------------------

A good test usually checks one main idea. If a test reads data, transforms it,
writes it to disk, reads it again, plots it, and checks five unrelated
properties, it becomes hard to understand why the test failed.

Start with a clear test name:

.. code-block:: python

   def test_invalid_osm_pbf_raises_meaningful_error(tmp_path):
       ...

The name tells us what behaviour the test protects. This is useful when the
test fails in CI: the failing test name already gives the developer a first
hint.

Use fixtures for repeated setup
-------------------------------

If several tests need the same sample file or object, move that setup into a
fixture. This keeps each test focused on the behaviour being checked:

.. code-block:: python

   @pytest.fixture
   def small_network():
       osm = OSM(get_data("test_pbf"))
       return osm.get_network(nodes=True)

Once the fixture exists, tests can ask for ``small_network`` as an argument.
This avoids copying the same setup code into many places.

Be careful with slow integration tests
--------------------------------------

An **integration test** checks that several parts of the system work together.
These tests are valuable, but they are often slower and more fragile than small
unit tests. Pyrosm has live download tests, but it does not run them in every CI
job. The workflow turns them on only for one selected runner with the
``RUN_DOWNLOAD_TESTS`` environment variable.

This pattern works well:

- Run small unit tests on every pull request.
- Run integration tests in CI, but keep them separate from the fastest tests.
- Run live-service tests only when needed or only in one selected job.
- Mark skipped tests clearly so everyone understands why they did not run.

Avoid testing implementation details
------------------------------------

Tests should usually protect public behaviour, not internal code structure. If a
test depends too much on private helper functions or internal variable names, it
can fail when you refactor the package even though users see the same behaviour
as before.

Prefer tests such as:

- "Calling this public function returns a ``GeoDataFrame`` with these columns."
- "Passing an invalid path raises ``ValueError`` with a useful message."
- "The graph export contains the same number of nodes as the input table."

Use internal tests when the internal logic is complex and important, but do not
let them replace tests of the public API.

Keep expected results stable
----------------------------

Tests are easiest to trust when their expected results are stable. For spatial
data, exact values can sometimes differ slightly between platforms or dependency
versions because of floating-point calculations. Pyrosm handles some of these
cases by accepting a small range of expected rounded values.

Use exact checks when exactness matters. Use approximate checks when tiny
numerical differences are acceptable:

.. code-block:: python

   assert round(distance, 0) in [499, 500]

The important point is to be explicit. A future developer should understand
whether the test requires an exact value or allows a small tolerance.

Make failures useful
--------------------

A failing test should help the developer find the problem. Clear test names,
small inputs, and focused assertions all make failures easier to interpret.
When checking errors, test the exception type and, when useful, part of the
message:

.. code-block:: python

   with pytest.raises(ValueError, match="not available"):
       get_data("file_not_existing")

This checks both that the package fails and that it fails in a way that helps
the user.

To recap
--------

Good testing practice is mostly about discipline:

- Keep tests fast.
- Use small bundled sample data.
- Test one behaviour at a time.
- Separate fast unit tests from slow integration tests.
- Prefer public behaviour over implementation details.
- Make failures easy to understand.

With these habits in place, tests become a normal part of development rather
than a special task that happens only before a release.
