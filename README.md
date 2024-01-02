# shareable-science
A respository for testing some shareable, reproducible scientific software tools and services.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks)
[![shareable-science](https://github.com/timghill/shareable-science/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/timghill/shareable-science/actions/workflows/python-app.yml)
[![Deploy static content to Pages](https://github.com/timghill/shareable-science/actions/workflows/static.yml/badge.svg)](https://github.com/timghill/shareable-science/actions/workflows/static.yml)

This repo shows several good (not necessarily best) practices:

 * Working on the `dev` branch to maintain a clean `main` branch and merging with Pull Requests or `git merge` on the command line
 * Writing functional code in the `src/` directory and importing this into analysis `notebooks/` via the `setup.py` file
 * Online execution using [mybinder.org](https://mybinder.org/)
 * Online documentation using GitHub Pages: [timghill/github.io/shareable-science](https://timghill.github.io/shareable-science/)
   * The documentation inlucdes a static rendering of notebooks as well as links to the interactive versions
 * Contiguous Integration (CI) (i.e., automated testing on each push to `main` using a GitHub action)

## Installation

You can run the code and notebooks locally (in addition to online with [mybinder.org](https://mybinder.org/)) just like with any other project. This is a pure python package so installation is straightforward. The code is built to install using a `setup.py` script or with `pip`.

First, clone the repository

```bash
git clone https://github.com/timghill/shareable-science.git
```

Then navigate into the `shareable-science/` root. We need to install the `src/` python contents. Move into the `src/` directory and run `setup.py install`:

```bash
cd src/
sudo python3 setup.py install
```

Or, if you don't have root priveleges, add the `--user` flag to a `pip install` command (from inside the `src/` directory)

```bash
pip3 install . --user
```

Now you should be able to import the `src` package from python. You can test this interactively,

```bash
python3
>>> import src
```

To run and explore the notebooks, start a jupyter notebook server as usual,

```bash
jupyter notebook
```

and start exploring the `notebooks/` directory!

### Requirements

See `requirements.txt`. Local installation requires `numpy`, `matplotlib`, and `cmocean`.

## Documentation

An important aspect of this project is the automatic documentation generation using [sphinx](https://www.sphinx-doc.org/en/master/) and online hosting with [GitHub pages](https://pages.github.com/). The documentation info is all maintained under the `docs/` directory. The documentation source code is in (`docs/source/`) and the static html is built to (`docs/build/`). The static html files are hosted oneline using GitHub pages: [https://timghill.github.io/shareable-science/](https://timghill.github.io/shareable-science/), using a GitHub action that is triggered by pushing to the `main` branch.

### Updating the documentation

After updating the documentation source files (in `docs/source/`), the html files can be regenerated using the sphinx Makefile. From the documentation root (`docs/`), run

```bash
make html
```

to rebuild the static html documentation. This generates new html files in `build/html`. Pushing these to the main branch will trigger the online docs to be updated.

The docs are built using [sphinx](https://www.sphinx-doc.org/en/master/) with extensions:

 * `sphinx.ext.autodoc` and `sphinx.ext.autosummary` for automatic documentation generation,
 * `sphinx.ext.napoleon` for reading [numpy style docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html),
 * `myst_parser` for reading markdown files,
 * `nbsphinx` for including python notebooks (see next section).

 Note: if you've updated the contents or naming of the source code, you need to:

  * Reinstall the source code (with `pip install --user .` for example),
  * Regenerate the autosummaries,
    ```bash
    sphinx-apidoc -f -o source/ ../src
    ```
  * Then remake the docs with `make html`.


## Online notebooks running with `mybinder`

This repo also explores using `mybinder` to run the code online, with no local installation required. You can run the code with `mybinder` by simply navigating to the appropriate url. To run the `dev` branch notebooks, go to [mybinder.org/v2/gh/timghill/shareable-science/dev?labpath=notebooks](https://mybinder.org/v2/gh/timghill/shareable-science/dev?labpath=notebooks)

To run the `main` branch notebooks, replace `dev` with `main`, [mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks](https://mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks).

## Usage

For now, the package `src/` does not contain any scientifically interesting code. The function `src.run_simulation()` simply returns a 100 x 100 array of normally distributed random numbers. Replace this module with any functional code for your project and document it here!

## Testing

TODO. Explain testing with `pytest` and GitHub action (`.github/workflows/python-app.yml`).

## Scalable directory structure

For a larger project, the full directory structure might look more like

```
.git
.gitignore

LICENSE
README.md
requirements.txt                # Python requirements

setup.py                        # Instructions to install using python3 setup.py install or pip3 install

build/                          # Created by installing with setup.py. Not under version control
src.egg-info                    # Created by installing with setup.py. Not under version control

src/                            # Any source code, functions, modules, classes, etc. Might be broken down further
    __init__.py
    modules.py
    ...

data/
    raw/                        # Raw source data (never manipulated!)
    processed/                  # Processed, analysis-ready data

notebooks/
    01_th_analysis01.ipynb
    02_th_analysis02.ipynb
    ...

docs/
    report.pdf                  # Compiled PDF reports, papers, preprints, etc.
```

Tim Hill
December 2023
