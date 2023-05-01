# テンプレートしたい

```console
$ myst templates list
```

デフォルトで用意されているテンプレートの一覧を確認できます。
``--site`` / ``--pdf`` / ``--tex``や``--tag``のオプションを使って、検索結果をフィルターできます。

## ウェブサイトのテンプレートしたい

```console
$ myst templates list --site

Book Theme               site/myst/book-theme
Description: Simple site for displaying multiple articles and notebooks with a table of contents.
Tags: book

Article Theme            site/myst/article-theme
Description: Simple site for displaying an article with associated notebooks.
Tags: book

$ myst templates list --site book-theme
Book Theme               book-theme
ID: site/myst/book-theme
Version: 1.0.0
Authors: Rowan Cockett
Description: Simple site for displaying multiple articles and notebooks with a table of contents.
Tags: book

Parts:

Options:
hide_toc (boolean) - Hide the table of contents
twitter (string) - Twitter handle related to the site
logo (file) - Local path to logo image
logo_text (string) - Short text to display next to logo at the top of all pages
analytics_google (string) - Google analytics key
analytics_plausible (string) - Plausible analytics key
```

``--site``オプションをつけるとウェブサイトのテンプレート名を確認できます。
テンプレート名を指定すると、設定可能なオプションなどを確認できます。

## PDFのテンプレートしたい

```console
$ myst templates list --pdf

$ myst templates list --pdf arxiv_two_column
arXiv (Two Column)       arxiv_two_column
ID: tex/myst/arxiv_two_column
Version: 1.0.0
Authors: Brenhin Keller
Description: A two column arXiv compatible template
Tags: paper, two-column, preprint, arxiv, bioarxiv, eartharxiv

Parts:
abstract (required) - Keep it short — abstracts longer than 1920 characters will not be accepted; abridge your abstract if necessary
acknowledgments - Free form acknowledgments section will be include at the end of the article

Options:
link (string) - Include a link back to the article on curvenote.com. This link will be placed inline at the end of all content, before the bibliography section.

$ myst templates list --pdf curvenote
Curvenote Default        curvenote
ID: tex/myst/curvenote
Version: 0.2.1
Authors: Steve Purves
Description: A paper styled template using the custom environments and styling to match Curvenote Web
Tags: article, paper

Parts:
abstract - An abstract is a short summary of your research paper or report. A good abstract will prepare readers for
	the detailed information to follow, communicate the essence of the article and help readers take away and
	remember key points.
acknowledgments - You can this section to highlight support such as; collaborations, data sources, funding sources, broader
	projects. This section will be places towards the end of the article with a subtitle - Acknowledgments.

Options:
link (string) - Link to the article online as a footnote on the first page
```

``--pdf``オプションを使って、PDFのテンプレート名を確認できます。
テンプレート名を指定すると、設定可能なオプションや指定可能なブロック要素名を確認できます。
