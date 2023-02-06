# 章見出しを変更したい

```python
latex_elements["preamble"] += "\\renewcommand{\\thesection}{見出しだよ。第\\arabic{section}章}"
```

Sphinxで生成したPDFの見出しが「第ONE （1章タイトル）」のようになっています。
[LaTeXで章見出しを変更する方法](../latex/latex-section.md)）と同じように章見出しを再定義して変更できないか試してみたのですが、ダメでした。

```{note}
上記の設定で、本文中の章見出しは変更できていました。
なので、別のパッケージ／コマンドに依存しているっぽいです。
引き続き調査する。
```
