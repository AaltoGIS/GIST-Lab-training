# GIST Lab Training

This folder contains short Sphinx-based learning materials about testing,
packaging, and continuous integration for Python libraries, using
[`pyrosm`](https://github.com/pyrosm/pyrosm) as the running example.

Build the site locally with:

```bash
python -m pip install -r docs/requirements.txt
python -m sphinx -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser after the build finishes.
