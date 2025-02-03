# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xxx'
copyright = '2025, hotchilipowder'
author = 'hotchilipowder'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "myst_parser",
  "sphinx.ext.autodoc",
  "sphinx.ext.intersphinx",
  "sphinx.ext.extlinks",
  "sphinx.ext.todo",
  "sphinx.ext.viewcode",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_copybutton",
  "sphinxcontrib.bibtex",
  "sphinxcontrib.mermaid",
  "sphinxemoji.sphinxemoji",
]

html_css_files = [
 "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

bibtex_bibfiles = ['refs.bib']

myst_enable_extensions=[
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_words_per_minute = 10

comments_config = {
   # "utterances": {
   #    "repo": "EZEORG/dev_zero_to_hero",
   #    "optional": "config",
   # }
}


templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

language = 'zh'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']


