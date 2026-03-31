# あいまい検索したい（`orderless`）

```emacs
(use-package orderless
  :ensure t
  :custom
  (completion-styles '(orderless basic))
  (company-category-overrides
    '((file (styles basic partial-completion)))
  )
  (orderless-matching-styles
    '(orderless-prefixes orderless-regexp orderless-literal)
  )
)
```

`orderless`は、補完機能を拡張し「あいまい検索（fuzzy search））できるようにするパッケージです。
単語をスペースで区切ることでAND検索できます。
ミニバッファーなどに表示されたアイテムを絞り込むのに使えます。
[vertico](./emacs-vertico.md)と併用するのが一般的です。

:::{seealso}

- `ido`
- `ivy`
- `fussy`
- `flex`

:::
