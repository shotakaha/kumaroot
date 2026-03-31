# あいまい検索したい（`ido` / `ido-vertical-mode`）

```emacs
(use-package ido
  :init
  (ido-mode 1)
  (ido-everywhere 1)
  :custom
  ;; あいまい検索を有効にする
  (ido-enable-flex-matching t)
  ;; ファイル探索を賢くする
  (ido-use-filename-at-point 'guess)
  (ido-create-new-buffer 'always)
  ;; 最近開いたファイルも候補にする
  (ido-use-virtual-buffers t)
)

(use-package ido-vertical-mode
  :after ido
  :init
  (ido-vertical-mode 1)
  :custom
  (ido-vertical-define-keys 'C-n-C-p-only)
)
```

`ido`はミニバッファーであいまい検索できるようになる標準パッケージです。
`ido-vertical-mode`を有効にすると、検索候補を縦に表示できます。

:::{seealso}

- `ivy` + `counsel`
- `vertico` + `orderless`

現在は`vertico` + `orderless`を選択するのがよいです。

:::
