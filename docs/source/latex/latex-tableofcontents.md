```{eval-rst}
.. index::
    pair: LaTeX; 目次したい
```

# 目次したい（``\tableofcontents``）

```latex
\tableofcontents  % 目次（章・節など）
\listoffigures    % 図目次
\listoftables     % 表目次
```

:::{seealso}

- [](../hugo/hugo-tableofcontents.md)
- [](../myst/myst-toc.md)
- [](../sphinx/sphinx-syntax-toctree.md)
- [](../typst/typst-outline.md)

:::


## 目次の深さを変更したい

```latex
% プリアンブル
\setcounter{tocdepth}{1}  % \sectionまで表示
\setcounter{tocdepth}{2}  % \subsectionまで表示
```

## 目次を書き換えたくない

```latex
% プリアンブル
\nofiles
```
