#Adapted from the sphinx-tutorial and https://github.com/tomography/tomobank/blob/master

# Configuration file for the Sphinx documentation builder.
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.


import sphinx_rtd_theme
import os, sys
sys.path.insert(0, os.path.abspath('..'))

# We require sphinx >=2 because of sphinxcontrib.bibtex,
needs_sphinx = '2.0'

# -- Project information -----------------------------------------------------
# General information about the project.
Affiliation = u'Goyal Lab'
project = u'SingletCode'
copyright = u'2023, ' + Affiliation

# The full version, including alpha/beta/rc tags
currentVersion = open("VERSION").read().strip()
release = currentVersion


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.bibtex',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_size',
]
sphinx_rtd_size_width = "90%"

bibtex_bibfiles = [
    'bibtex/ref.bib'
]

todo_include_todos=True


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# conf.py

html_theme_options = {
    "style_external_links": True
}

bibtex_bibfiles = [
    'bibtex/ref.bib',
    ]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

#Thinsg for sphinx-toolbox
