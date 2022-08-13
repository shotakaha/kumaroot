# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'KumaROOT'
author = 'Shota TAKAHASHI'
copyright = '2015 - 2022, Shota TAKAHASHI'
version = '0.6.0'
release = '0.6.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'ja'

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
#     }
# source_encoding = 'utf-8-sig'
root_doc = "index"
numfig = True

# 図表番号表示のカスタム設定
# フォーマット文字列を辞書型で指定
# デフォルトの設定を書いた後、カスタム設定で上書き
numfig_format = {
    'figure' : 'Fig. %s',
    'table' : 'Table %s',
    'code-block' : 'Listing %s'
}
numfig_format['figure'] = '図 %s'
numfig_format['table'] = '表 %s'
numfig_format['code-block'] = 'コードサンプル %s'

# 図表番号のスコープ
# 0: 全てのドキュメントで通し番号
# 1: セクション毎に番号を付与（x.1, x.2, x.3, ...）
# 2: サブセクション毎に番号を付与（x.x.1, x.x.2, x.x.3, ...）
# デフォルトは 1
numfig_secnum_depth = 1

today_fmt = "%Y-%m-%d"

# -- Options for MyST Parser -------------------------------------------------

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# -- Options for Math -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

# math_number_all = False
# math_eqref_format = ""
# math_numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'analytics_id': 'G-F2T33GE7N3',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -*- coding: utf-8 -*-
#
# KumaROOT documentation build configuration file, created by
# sphinx-quickstart on Sat Jul 11 17:44:03 2015.
#

#################################################
# Options for sphinx.ext.todo
##################################################
todo_include_todos = True

# htmlhelp_basename = 'KumaROOTdoc'

##################################################
## Options for LaTeX output
##################################################
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_engine = 'lualatex'
latex_documents = [(
    root_doc,
    'KumaROOT.tex',
    'KumaROOT',
    'Shota TAKAHASHI',
    'manual'),
]
latex_docclass = {'manual' : 'jlreq'}
latex_toplevel_sectioning = "chapter"

latex_elements = {
    'papersize' : 'a4paper',
    'pointsize': '12pt',
    'preamble': '',
    'figure_align': 'htbp',
}

# latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
# latex_elements['preamble'] += '\\usepackage{graphics}\n'
# latex_elements['preamble'] += '\\hypersetup{bookmarksnumbered=true}\n'
# latex_elements['preamble'] += '\\hypersetup{bookmarksopen=true}\n'
# latex_elements['preamble'] += '\\hypersetup{bookmarksopenlevel=2}\n'
# latex_elements['preamble'] += '\\hypersetup{colorlinks=true}\n'
# latex_elements['preamble'] += '\\hypersetup{pdfpagemode=UseOutlines}\n'

# latex_elements['preamble'] += '\\renewcommand{\\familydefault}{\\sfdefault}\n'
# latex_elements['preamble'] += '\\renewcommand{\\kanjifamilydefault}{\\gtdefault}\n'
# latex_logo = './images/toumin_kuma.png'
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_appendices = []
#latex_domain_indices = True

#################################################
## Options for Epub output
##################################################

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
#epub_basename = project
#epub_theme = 'epub'
#epub_language = ''
#epub_scheme = ''
#epub_identifier = ''
#epub_uid = ''
#epub_cover = ()
#epub_guide = ()
#epub_pre_files = []
#epub_post_files = []
epub_exclude_files = ['search.html']
#epub_tocdepth = 3
#epub_tocdup = True
#epub_tocscope = 'default'
#epub_fix_images = False
#epub_max_image_width = 0
#epub_show_urls = 'inline'
#epub_use_index = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
