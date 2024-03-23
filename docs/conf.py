#Adapted from the sphinx-tutorial and https://github.com/tomography/tomobank/blob/master

# Configuration file for the Sphinx documentation builder.
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.


import sphinx_rtd_theme
import os, sys
from sphinx.writers.html5 import HTML5Translator
from docutils import nodes
from docutils.nodes import Element

sys.path.insert(0, os.path.abspath('..'))

# We require sphinx >=2 because of sphinxcontrib.bibtex,
needs_sphinx = '2.0'

# -- Project information -----------------------------------------------------
# General information about the project.
Affiliation = u'Goyal Lab'
project = u'singletCode'
copyright = u'2023, ' + Affiliation

# The full version, including alpha/beta/rc tags
currentVersion = open("./VERSION").read().strip()
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
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
sphinx_rtd_size_width = "90%"

bibtex_bibfiles = [
    './bibtex/ref.bib'
]

todo_include_todos=True
add_module_names = False

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


# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# html_theme_options = {
#     "style_external_links": True
# }

bibtex_bibfiles = [
    './bibtex/ref.bib',
    ]

class PatchedHTML5Translator(HTML5Translator):

    def visit_reference(self, node: Element) -> None:
        atts = {'class': 'reference external'}
        if node.get('internal') or 'refuri' not in node:
            atts['class'] = 'reference internal'
        else:
            # Customize behavior for external links
            atts['target'] = '_blank'
            atts['rel'] = 'noopener noreferrer'

        if 'refuri' in node:
            atts['href'] = node['refuri'] or '#'
            if self.settings.cloak_email_addresses and atts['href'].startswith('mailto:'):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = True
        else:
            assert 'refid' in node, 'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']

        if 'reftitle' in node:
            atts['title'] = node['reftitle']

        if 'target' in node and 'target' not in atts:
            atts['target'] = node['target']

        self.body.append(self.starttag(node, 'a', '', **atts))
        HTML5Translator.visit_reference(self, node)
def setup(app):
    app.set_translator('html', PatchedHTML5Translator)
    app.add_js_file(None, body="document.addEventListener('DOMContentLoaded', function() {document.querySelectorAll('a.reference.external').forEach(function(a) {a.setAttribute('target', '_blank'); a.setAttribute('rel', 'noopener noreferrer');});});", type="text/javascript")

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

#Thinsg for sphinx-toolbox
