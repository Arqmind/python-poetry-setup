# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# pylint: disable=C0103

"""
Documentation Configuration
===========================

Define the configuration options for the Sphinx documentation.
"""
import os
import sys

sys.path.insert(0, os.path.abspath("../"))
project = 'Python Poetry Setup'
copyright = '2023, Arqmind'
author = 'BChathoth <bchathoth@arqmind.com>'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

build_dir = "build"
templates_path = [".templates"]
exclude_patterns = [".build", "Thumbs.db", ".DS_Store", "**/tests"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_output = 'html'
html_theme = 'pyramid'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
