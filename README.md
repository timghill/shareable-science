# shareable-science
A respository for testing some shareable, reproducible scientific software tools and services.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks)

This repo shows several good (not necessarily best) practices:

 * Working on the `dev` branch to maintain a clean `main` branch and merging with Pull Requests or `git merge` on the command line
 * Writing functional code in the `src/` directory and importing this into analysis `notebooks/` via the `setup.py` file
 * Online execution using [mybinder.org](https://mybinder.org/)

## Local installation

You can run the code and notebooks locally, just like with any other project. This is a pure python package so installation is straightforward. At this time, the only supported installation is by directly cloning,

```bash
git clone https://github.com/timghill/shareable-science.git
```

Now, navigate into the `shareable-science/` root. We need to install the `src/` python contents. Don't worry, this is not hard! You just need to do

```bash
sudo python3 setup.py install
```

Or, if you don't have root priveleges, add the `--user` flag to a `pip install` command,

```bash
pip3 install . --user
```

Then, start a jupyter notebook server as usual,

```bash
jupyter notebook
```

and start exploring!

### Requirements

See `requirements.txt`. Local installation requires `numpy`, `matplotlib`, and `cmocean`.

## Running with `mybinder`

The real purpose of this repo is to explore using `mybinder` to run the code online, with no local installation required. You can run the code with `mybinder` by simply navigating to the appropriate url. To run the `dev` branch notebooks, go to [mybinder.org/v2/gh/timghill/shareable-science/dev?labpath=notebooks](https://mybinder.org/v2/gh/timghill/shareable-science/dev?labpath=notebooks)

To run the `main` branch notebooks, replace `dev` with `main`, [mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks](https://mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks)

## Usage

For now, the package `src/` does not contain any scientifically interesting code. The function `src.run_simulation()` simply returns a 100 x 100 array of normally distributed random numbers. Replace this module with any functional code for your project!

## Directory structure

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