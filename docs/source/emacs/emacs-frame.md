# フレームしたい（`set-frame-size`）

```text
M-x set-frame-size
```

`set-frame-size`コマンドで、フレーム（＝ウィンドウ）の大きさを変更できます。
ミニバッファーに横幅（`Width:`）と高さ（`Height:`）を入力します。
単位はピクセル数ではなく、文字数です。

## 起動時に設定したい

```emacs-lisp
(use-package emacs
  :init
  ;; 初期フレームサイズ
  (add-to-list 'default-frame-alist '(width . 100))
  (add-to-list 'default-frame-alist '(height . 40))
)
```

起動時のサイズを変更したい場合は、`init.el`で設定できます。

```emacs-lisp
(use-package emacs
  :init
  ;; 初期フレームサイズ
  (add-to-list 'default-frame-alist '(width . 100))  ;; 文字数
  (add-to-list 'default-frame-alist '(height . 40))  ;; 文字数
  (add-to-list 'default-frame-alist '(left . 100))   ;; ピクセル数
  (add-to-list 'default-frame-alist '(top . 50))     ;; ピクセル数
)
```

起動時に表示する位置も変更できます。
位置指定の単位はピクセル数です。
