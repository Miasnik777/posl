
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'djangotutorial')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'typingstats'
copyright = '2025, misha'
author = 'misha'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints', 
    'sphinxcontrib_django', 
]
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'show-inheritance': True,
}
templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
