# Docs for `shareable-science`

This directory contains source and build directories for automatic documentation built with sphinx from the python source code. See the docs source (`source/`) and static html (`build/`) directories.

## Building the documentation

From `./source/`, run

```bash
make html
```

to rebuild the static html documentation. This generates the html files in `build/html`.

The docs are built using [sphinx](https://www.sphinx-doc.org/en/master/) with extensions

 * `sphinx.ext.autodoc` and `sphinx.ext.autosummary` for automatic documentation generation,
 * `sphinx.ext.napoleon` for reading [numpy style docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html),
 * `myst_parser` for reading markdown files,
 * `nbsphinx` for including python notebooks (see next section).

## Python notebooks

This documentation uses a trick to render static python notebooks using the `nbsphinx` extension. Once you've added this extension to `docs/conf.py`, ...
