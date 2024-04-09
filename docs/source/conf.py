# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "KumaROOT"
author = "Shota TAKAHASHI"
copyright = "2015 - 2024, Shota TAKAHASHI"
version = "1.33.0"
release = "1.33.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_tags",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]
exclude_patterns = []
language = "ja"

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
#     }
# source_encoding = 'utf-8-sig'
nitpicky = True

numfig = True

# 図表番号表示のカスタム設定
# フォーマット文字列を辞書型で指定
# デフォルトの設定を書いた後、カスタム設定で上書き
numfig_format = {"figure": "Fig. %s", "table": "Table %s", "code-block": "Listing %s"}
numfig_format["figure"] = "図 %s"
numfig_format["table"] = "表 %s"
numfig_format["code-block"] = "コード %s"

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

myst_html_meta = {
    "description lang=ja": "KumaROOTです。ちょっとだけROOTを使ったことがある学生や研究者が対象。「逆引き辞典」として使えるようにしたいと思います。",
    "keywords": "ROOT, Python",
}

myst_number_code_blocks = [
    "bash",
    "cpp",
    "dockerfile",
    "md",
    "python",
    "rst",
    "toml",
    "typst",
]

# -- Options for Math -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math

# math_number_all = False
# math_eqref_format = ""
# math_numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_title = f"{project} v{version}"
html_logo = "./_static/quma.jpeg"
html_static_path = ["_static"]
html_css_files = ["css/heading.css"]
html_theme_options = {
    "analytics_id": "G-F2T33GE7N3",  #  Provided by Google in your dashboard
    "prev_next_buttons_location": "both",
    "style_external_links": True,
    "style_nav_header_background": "darkorange",
}


# -- Options for OGP --------------------------------------------------

ogp_site_url = "https://kumaroot.readthedocs.io/ja/latest/"
ogp_image = "./_static/quma.jpeg"
ogp_use_first_image = True
ogp_enable_meta_description = True
ogp_social_cards = {
    "enable": True,
    "font": "Noto Sans CJK JP",
}

# -- Options for Sphinx Tags --------------------------------------------------

tags_create_tags = True
# tags_output_dir = "_tags"
tags_extention = ["md"]
# tags_overview_title = "Site tags"
# tags_intro_text = "Tags"
# tags_page_title = "My Tags"
# tags_page_header = "With this tag"
# tags_index_head = "Tags"
tags_create_badges = True
# tags_badge_colors = {}

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
# Options for LaTeX output
##################################################
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_engine = "lualatex"
latex_docclass = {
    "howto": "ltjsreport",
    "manual": "ltjsreport",
}

# latex_toplevel_sectioning = "part"

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    # "extraclassoptions": "tombow",
    "fontpkg": "",
    "extrapackages": "",
    "preamble": "",
    "polyglossia": "",
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
}

# Loaded before hyperref
latex_elements["extrapackages"] = r"""
\usepackage{physics}
"""

# Loaded after hyperref
latex_elements["preamble"] = r"""
\setlength{\footskip}{3\zw}
\hypersetup{bookmarksnumbered=true}
\hypersetup{bookmarksopen=true}
"""
# \hypersetup{colorlinks=true}

# latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
# latex_elements['preamble'] += '\\hypersetup{bookmarksopenlevel=2}\n'

# latex_elements['preamble'] += '\\hypersetup{pdfpagemode=UseOutlines}\n'

# latex_elements['preamble'] += '\\renewcommand{\\familydefault}{\\sfdefault}\n'
# latex_elements['preamble'] += '\\renewcommand{\\kanjifamilydefault}{\\gtdefault}\n'
latex_logo = "./_static/quma.jpeg"
# latex_use_parts = True
latex_show_pagerefs = True
latex_show_urls = "footnote"
# latex_appendices = []
# latex_domain_indices = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"python": ("https://docs.python.org/", None)}
