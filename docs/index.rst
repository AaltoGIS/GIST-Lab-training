:html_theme.sidebar_secondary.remove:

GIST Lab Training
=================

.. rst-class:: lead

    Short, practical training materials for **doing research software and
    research with AI well** — from the mechanics of a maintainable Python
    library to the responsible and efficient use of AI in a research group.

These materials collect the day-to-day skills we lean on in the lab. Each
**theme** below is a self-contained module: a set of short pages you can read in
order or dip into when a specific question comes up. The examples are concrete
and drawn from real tools and workflows, so the vocabulary you learn here maps
directly onto your own projects.

.. grid:: 1 2 2 2
    :gutter: 4
    :class-container: sd-text-center

    .. grid-item-card:: Testing and packaging Python libraries
        :link: testing_packaging/index
        :link-type: doc
        :class-card: sd-border-0

        Why tests matter, the testing vocabulary, packaging a library for
        PyPI, and running it all automatically with GitHub Actions. Uses
        ``pyrosm`` as the running example.

    .. grid-item-card:: Responsible and efficient use of AI for research
        :link: ai_research/index
        :link-type: doc
        :class-card: sd-border-0

        Where AI tools genuinely help, how to get good results without
        wasting effort, and how to stay honest, transparent, and
        reproducible while doing it.

.. toctree::
    :hidden:
    :maxdepth: 1

    Testing and packaging <testing_packaging/index>
    AI for research <ai_research/index>
