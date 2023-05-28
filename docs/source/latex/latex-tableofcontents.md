```{eval-rst}
.. index::
    pair: LaTeX; toc
```

# 目次を作成したい（``\tableofcontents``）

```latex
\tableofcontents  % 目次（章・節など）
\listoffigures    % 図目次
\listoftables     % 表目次
```

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
