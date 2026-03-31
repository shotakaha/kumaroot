# フォントしたい（`set-frame-font`）

```emacs
(use-package emacs
  :init
  (set-face-attribute 'default nil
    :family "HackGen"
    :height 140
  )
)
```

GUI版を使っている場合、フォントを変更できます。
（CUI版はターミナルのフォントから変更できません）

## 日本語フォントしたい（`japanese-jisx0208`）

```emacs
(use-package emacs
  :init
  ;; 英字フォント
  (set-face-attribute 'default nil
    :family "JetBrains Mono"
    :height 140
  )
  ;; 日本語フォント
  (set-fontset-font t 'japanese-jisx0208
    (font-spec :family "Noto Sans CJK JP"))
  )
```

`set-fontset-font`で、日本語フォントを設定できます。
