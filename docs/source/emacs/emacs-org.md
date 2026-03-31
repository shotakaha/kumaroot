# Org-modeの使い方

```emacs
(use-package org
  :ensure t
  :custom
  (org-directory "~/org/")  ;; Org用ディレクトリ
  (org-agenda-files (list "~/org/"))  ;; アジェンダの対象ファイル
  (org-log-done 'time)      ;; DONEにした時刻を記録
  (org-startup-indented t)  ;; インデント表示
  :bind
  (("C-c a" . org-agenda)
  ("C-c c" . org-capture))
)
```

`org-mode`はEmacs標準の「アウトラインモード」ですが、それ以上のことがたくさんできます。
とても多機能なので詳しくは``M-x org-info``でドキュメントを確認してください。

```{toctree}
emacs-org-latex
```
