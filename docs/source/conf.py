# Configuration file for the Sphinx documentation builder.
import sys
sys.path.insert(1, '../..')
import csv2doc

# -- Project information

project = 'ROS Documentation'
copyright = '2025, Jeremy Wang'
author = 'Jeremy Wang'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Start main script
print("Testing in config.")

path = '../../data.csv'

processed_data = csv2doc.preprocess_csv(path)

csv2doc.generate_rst_file(processed_data)

print("End of script...")
