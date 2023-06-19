# 段落したい

```latex
%% プリアンブル
\setlength{\linewidth}{40\zw}     % 1行の長さ
\setlength{\baselineskip}{1.5\zw} % 行送りの大きさ（＝行間の高さ）
\setlength{\parindent}{1\zw}      % 段落のインデント
\setlength{\parskip}{1\zw}        % 段落の間の高さ
```

ドキュメントクラスのデフォルトの段落設定が好みでない場合は、この辺りの長さを調整してみるとよいでしょう。
和文の場合は長さの単位を``zw（zenkaku width）``とするとだいたいきれいに揃います。

より詳しく知りたい場合は[Overleafのドキュメント](https://www.overleaf.com/learn/latex/Articles/How_to_change_paragraph_spacing_in_LaTeX)を参考にするとよいでしょう。

```{toctree}
---
maxdepth: 1
---
latex-linebreak
latex-flushright
latex-booktabs
latex-xcolor
latex-bxjalipsum
latex-minted
```
