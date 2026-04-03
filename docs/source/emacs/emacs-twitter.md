# Twitterしたい（`twittering-mode`）

```emacs-lisp
(use-package twittering-mode
  :ensure t
  :init
  (setq twittering-use-master-password t)

  :custom
  ;; 表示件数
  (twittering-number-of-tweets-on-retrieval 50)
  ;; アイコン表示をOFF
  (twittering-icon-mode nil)

  :config
  ;; 初期表示するタイムライン
  (setq twittering-initial-timeline-spec-string ":home")

  :bind
  (("C-c t" . twittering-get-and-render-timeline))  ;; タイムライン取得
)
```

`twittering-mode`はEmacsでTwitterできる拡張パッケージです。
最近はTwitterをやってる人も多いと思いますが、
息抜きのときにもEmacsを使うことで、操作方法などを覚えることができます。

:::{warning}

TwitterからXになりAPI仕様が変更されました。
おそらく現在は動作しないパッケージです。

:::
