# shareable-science
A respository for testing some shareable, reproducible scientific software tools and services.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks)

This repo shows several good (not necessarily best) practices:

 * Working on the `dev` branch to maintain a clean `main` branch and merging with Pull Requests or `git merge` on the command line
 * Writing functional code in the `src/` directory and importing this into analysis `notebooks/` *Not implemented yet. Need the module to be installable by `mybinder`*
 * Online execution using [mybinder.org](https://mybinder.org/)

## Running locally

You can run the code and notebooks locally, just like with any other project. First, if you've changed the source in `modules/`, re-install the python package,

```bash
sudo python3 setup.py install
```

Then, start a jupyter notebook server as usual,

```bash
jupyter notebook
```

## Running with `mybinder`

You can run the code online using `mybinder` by simply navigating to the appropriate url. To run the `dev` branch notebooks, go to
```
https://mybinder.org/v2/gh/timghill/shareable-science/dev?labpath=notebooks
```

To run the `main` branch notebooks, replace `dev` with `main`,
```
https://mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks
```

