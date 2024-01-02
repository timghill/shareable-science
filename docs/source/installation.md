# Installation

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

## Requirements

See `requirements.txt`. Local installation requires `numpy`, `matplotlib`, and `cmocean`.
