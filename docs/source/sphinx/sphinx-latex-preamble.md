# プリアンブルを設定する（``latex_elements['preamble']``）

``latex_elements`` の``preamble``に複数のパッケージを書くと可読性が下がるため、
以下のように``latex_elements['preamble']``にパッケージ単位で追加して書くことにしています。

単なる文字列として追加するため、パッケージ名の終わりには改行コード（``\n``）が必要です。

```python
latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
latex_elements['preamble'] += '\\usepackage{graphics}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksnumbered=true}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksopen=true}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksopenlevel=2}\n'
latex_elements['preamble'] += '\\hypersetup{colorlinks=true}\n'
latex_elements['preamble'] += '\\hypersetup{pdfpagemode=UseOutlines}\n'
```

``LaTeX`` 文書の出力は以下のようになります。

```latex
\usepackage{pxjahyper}
\usepackage{graphics}
\hypersetup{bookmarksopen=true}
\hypersetup{bookmarksopenlevel=2}
\hypersetup{colorlinks=true}
\hypersetup{pdfpagemode=UseOutlines}
```
