# YaTeXの使い方

YaTeX（野鳥）はEmacsでLaTeX文書を作成するためのパッケージです。
``MELPA`` からインストールできます。

## インストール
```emacs
M-x package-install RET yatex RET
```

## 設定

```lisp
(use-package yatex
    :ensure t
    :mode (("\\.tex$" . yatex-mode))
    :bind (("C-c C-t" . YaTeX-typeset-menu))
    :config
    ;; automatically selected according to current language
    ;; (setq YaTeX-japan t)

    ;; change default kanji-code from 2:JIS to 4:UTF-8
    ;; (setq latex-message-kanji-code 4)
    ;; (setq YaTeX-kanji-code 4)
    ;; (setq YaTeX-coding-system 4)

    ;; declared in yatexlib.el
    (setq YaTeX-inhibit-prefix-letter t)
    ;; local dictionary is NOT needed
    (setq YaTeX-nervous nil)

    ;; declared in yatex.el
    (setq tex-command "ptex2pdf -l -ot -synctex=1 -file-line-error")
    (setq bibtex-command "pbibtex")
    (setq dvi2-command "open -a Preview")    ;; use Preview.app
    (setq tex-pdfview-command "open -a Preview")
    (setq dviprint-command-format "dvipdfmx %s")
    (setq YaTeX-skip-default-reader t)
    (setq YaTeX-simple-messages t)
    ;; (setq YaTeX-template-file "...")
    )
```

## 拡張子が.texのファイルをyatex-modeで開く

```lisp
:mode (("\\.tex$" . yatex-mode))
```

## ローカル辞書は要らない

```lisp
(setq YaTeX-nervous nil)
```

## LaTeXコンパイラの設定

```lisp
(setq tex-command "ptex2pdf -l -ot -synctex=1 -file-line-error")
```
