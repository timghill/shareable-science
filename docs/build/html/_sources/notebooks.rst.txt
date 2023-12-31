Notebooks
=========

A list of links to non-interactive html rendered notebooks. The first example is rendered from a notebook directly inside the docs directory, while the second example is rendered from a notebook external to the docs directory; this second example is a little trickier to get running!

.. toctree::
   :maxdepth: 1 
   :caption: Notebook examples

   notebooks/notebook01
   notebooks/notebook

These notebooks can be viewed interactively using `binder <https://mybinder.org/v2/gh/timghill/shareable-science/main?labpath=notebooks>`_

Notebooks in the docs directory
-------------------------------

It's easy to include notebooks that are stored in the docs directory. If this page builds from ``docs/source/notebooks.rst``, and the notebook is ``docs/source/notebooks/notebook01.ipynb``, all we need to do is:

 #. Add the ``nbsphinx`` extension to ``docs/conf.py``, and
 #. Add a table of contents that includes ``notebooks/notebook01``.

See the source `directory tree <https://github.com/timghill/shareable-science/blob/main/docs/source/>`_.

External notebooks
------------------

By default, ``nbsphinx`` only looks for notebooks under the ``docs/source`` directory. But what if you have notebooks you've written in some other directory, maybe ``notebooks/``? We will use the `nbsphinx-link <https://nbsphinx-link.readthedocs.io/en/latest/>`_ extension to do include external notebooks.

 #. Install ``nbsphinx-link`` (Just a ``pip install nbsphinx-link``),
 #. Add ``nbsphinx_link`` to ``docs/conf.py``,
 #. For a notebook called ``mynotebook.ipynb`` (on some path outside of ``docs/source``), create a file ``mynotebook.nblink`` inside the docs source where you would like to link the notebook to. This file is a json file that just points to the notebook location, i.e. it looks like

   .. code-block::
      
      {
          "path": "path/to/mynotebook.ipynb"
      }

   where the path resolves correctly (this can take some trial and error...).

 #. Include this linked file in a table of contents as if it were the notebook.

    See the source directory tree linked above for the source for these examples!



