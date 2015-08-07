# -*- coding: utf-8 -*-
#
# SectionDoc documentation build configuration file, created by
# sphinx-quickstart on Wed Oct 26 10:59:39 2011.
#
# This file is executed with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sectiondoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosummary']

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SectionDoc'
copyright = u'2011, Enthought Inc'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.2'
# The full version, including alpha/beta/rc tags.
release = '0.2'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

autodoc_member_order = 'groupwise'
autoclass_content = 'both'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Output file base name for HTML help builder.
htmlhelp_basename = 'SectionDocdoc'

# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [(
    'index', 'SectionDoc.tex',
    u'SectionDoc Documentation', u'Ioannis Tziakos', 'manual')]

# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'refactordoc',
     u'SectionDoc Documentation', [u'Ioannis Tziakos'], 1)]


# -- Options for Epub output --------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'SectionDoc'
epub_author = u'Ioannis Tziakos'
epub_publisher = u'Ioannis Tziakos'
epub_copyright = u'2011, Ioannis Tziakos'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
