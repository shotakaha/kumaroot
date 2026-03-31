# YaTeXしたい（`yatex`）

```lisp
(use-package yatex
  :ensure t
  :mode (("\\.tex$" . yatex-mode))
  :bind (("C-c C-t" . YaTeX-typeset-menu))

  :custom
  ;; --- TeX engine
  (tex-command "latexmk -lualatex -synctex=1 -file-line-error")
  (bibtex-command "biber")
  ;; viewer (macOS)
  (dvi2-command "open -a Preview")
  (tex-pdfview-command "open -a Preview")

  ;; --- YaTeX behavior
  (YaTeX-inhibit-prefix-letter t)
  (YaTeX-nervous nil)
  (YaTeX-simple-message t)
  (YaTeX-skip-default-reader t)
  )
)
```

YaTeX（野鳥）はEmacsでLaTeX文書を作成するためのパッケージです。

## pLaTeXしたい

```lisp
(use-package yatex
  :ensure t
  :mode (("\\.tex$" . yatex-mode))
  :bind (("C-c C-t" . YaTeX-typeset-menu))
  :custom
  ;; declared in yatex.el
  (tex-command "ptex2pdf -l -ot -synctex=1 -file-line-error")
  (bibtex-command "pbibtex")
  (dvi2-command "open -a Preview")    ;; use Preview.app
  (tex-pdfview-command "open -a Preview")
  (dviprint-command-format "dvipdfmx %s")
  ;; declared in yatexlib.el
  (YaTeX-inhibit-prefix-letter t)
  ;; local dictionary is NOT needed
  (YaTeX-nervous nil)
  (YaTeX-skip-default-reader t)
  (YaTeX-simple-messages t)
  ;; (YaTeX-template-file "...")

  :config
  ;; Legacy settings from mixed JIS/UTF-8 encodings around 2010s
  ;; (setq YaTeX-japan t)
  ;; change default kanji-code from 2:JIS to 4:UTF-8
  ;; (setq latex-message-kanji-code 4)
  ;; (setq YaTeX-kanji-code 4)
  ;; (setq YaTeX-coding-system 4)
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
