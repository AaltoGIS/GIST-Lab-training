# Configuration file for the Sphinx documentation builder.

from datetime import datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

project = "GIST Lab Training"
author = "Henrikki Tenkanen"
current_year = datetime.now().year
copyright = f"{current_year}, Henrikki Tenkanen. Helpers: Claude and Codex."

extensions = [
    "sphinx.ext.mathjax",
    "IPython.sphinxext.ipython_console_highlighting",
    "myst_nb",
    "sphinx_design",
]

# MyST colon fences for admonitions and sphinx-design directives; GitHub-style
# heading anchors so in-page links resolve.
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 3

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML output -------------------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_title = "GIST Lab Training"

html_theme_options = {
    # GIST Lab logo in the navbar; the dark variant has the wordmark in white.
    "logo": {
        "image_light": "_static/GIST_Lab_logo_transparent.png",
        "image_dark": "_static/GIST_Lab_logo_dark.png",
    },
    # The top navbar is driven by the root toctree in index.rst.
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/AaltoGIS/GIST-Lab-training",
            "icon": "fa-brands fa-github",
        },
    ],
    "use_edit_page_button": True,
    "show_toc_level": 2,
    # Each theme opens to its own sub-sections in the sidebar rather than
    # showing the whole site at once.
    "navigation_depth": 3,
    "show_nav_level": 1,
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version", "theme-version"],
}

html_context = {
    "github_user": "AaltoGIS",
    "github_repo": "GIST-Lab-training",
    "github_version": "main",
    "doc_path": "docs",
}

# The landing page carries its own hero and cards; its sidebar would only
# repeat the navbar.
html_sidebars = {"index": []}

master_doc = "index"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
pygments_style = "sphinx"

# The materials are written as static lessons. If notebooks are added later,
# keep the convention of rendering stored outputs instead of executing
# notebooks during the documentation build.
nb_execution_mode = "off"
nb_execution_allow_errors = True
