# Configuration file for the Sphinx documentation builder.

from datetime import datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

project = "Testing and Packaging Python Libraries"
author = "Henrikki Tenkanen"
current_year = datetime.now().year
copyright = f"{current_year}, Henrikki Tenkanen"

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "myst_nb",
]

myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_book_theme"
html_title = ""
html_logo = ""
html_theme_options = {
    "repository_url": "https://github.com/pyrosm/pyrosm/",
    "repository_branch": "master",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "launch_buttons": {
        "binderhub_url": "",
        "notebook_interface": "jupyterlab",
        "collapse_navigation": False,
    },
}

master_doc = "index"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
pygments_style = "sphinx"

# The materials are written as static lessons. If notebooks are added later,
# keep the pyrosm convention of rendering stored outputs instead of executing
# notebooks during the documentation build.
nb_execution_mode = "off"
nb_execution_allow_errors = True
