# 基本設定したい（`emacs`）

```emacs
(use-package emacs
  :hook (prog-mode . display-fill-column-indicator-mode)
  :init    ;; 起動直後に実行
  (set-locale-environment "en_US.UTF-8")  ;; ロケール設定
  (set-language-environment "Japanese")   ;; お好みで

  (global-auto-revert-mode 1)    ;; ファイルの自動更新

  (menu-bar-mode -1)    ;; メニューバーを非表示
  (tool-bar-mode -1)    ;; ツールバーを非表示
  (scroll-bar-mode -1)  ;; スクロールバーを非表示
  (window-divider-mode 1)  ;; 画面分割時に境界を表示

  (global-display-line-numbers-mode 1)  ;; 行番号を表示
  (column-number-mode 1)    ;; 列番号を表示
  (show-paren-mode 1)       ;; 対応する括弧を強調
  (global-hl-line-mode 1)   ;; カーソル行をハイライト

  ;; カラムの目安（display-fill-columns-indicator-mode)
  (fill-column 80)    ;; 80列目に縦線を表示

  :config  ;; 初期化後に実行
  (fset 'yes-or-no-p 'y-or-n-p)    ;; yes/no -> y/n

  :custom  ;; 変数設定（setqの代わり）
  (inhibit-startup-screen t)     ;; スタート画面を表示しない
  (initial-scratch-message nil)  ;; scratchの初期メッセージを削除
  (ring-bell-function 'ignore)   ;; ビープ音を無効化

  (frame-resize-pixelwise t)    ;; フレームサイズをピクセル数に統一
  (fringe-mode 8)       ;; フレームの余白
  (line-spacing 0.2)    ;; 行間の大きさ
  (window-divider-default-right-width 2)    ;; 画面分割時の境界線の太さ
  (window-divider-default-bottom-width 2)   ;; 画面分割時の境界線の太さ

  (display-line-numbers-type 'relative)
  (show-paren-delay 0)
  (show-paren-style 'mixed)

  (indent-tabs-mode nil)    ;; タブを使わない（=スペースに置き換える）
  (tab-width 4)             ;; タブ幅

  (make-backup-files nil)    ;; バックアップをOFF
  (auto-save-default nil)    ;; 自動保存をOFF
  (create-lockfiles nil)     ;; ロックファイルをOFF

  (select-enable-clipboard t)    ;; EmacsとOSでクリップボードを共用

  (scroll-step 1)
  (scroll-conservatively 10000)

  :bind
  (
    ("C-h" . delete-backward-char)    ;; help-commandを上書き
    ("C-x k" . kill-current-buffer)   ;; kill-bufferを上書き
  )
)
```

`(use-package emacs)`で、Emacsの基本設定（ビルトイン設定）を変更できます。

:::{note}

この「`emacs`」はパッケージ名ではなく、
`use-package`がビルトイン機能を扱うために用意している特別な識別子です。
これにより、Emacs本体の設定も他のパッケージと同じ形式で整理できます。

:::

## UIを消したい

```emacs-lisp
(use-package emacs
  :init
  (menu-bar-mode -1)
  (tool-bar-mode -1)
  (scroll-bar-mode -1)
  (fringe-mode 8)

  :custom
  (line-spacing 0.2)    ;; 行間を広げる
  (frame-resize-pixelwise t)    ;;
)
```

メニューバー（`menu-bar-mode`）
ツールバー（`tool-bar-mode`）
スクロールバー（`scroll-bar-mode`）は非表示にすることが多いです。

`fringe-mode`でフレーム（＝ウィンドウ）の左右の余白を変更できます。
単位はピクセル数です。

## 画面分割したい（`window-divider-mode`）

```emacs-lisp
(use-package emacs
  :init
  (window-divider-mode 1)

  :custom
  (window-divider-default-right-width 2)
  (window-divider-default-bottom-width 1)
)
```

## 表示を補助したい

```emacs-lisp
(use-package emacs
  :init
  (global-display-line-numbers-mode 1)    ;; 行番号
  (column-number-mode 1)     ;; 列番号
  (show-paren-mode 1)        ;; 対応する括弧の強調
  (global-hl-line-mode 1)    ;; カーソル行のハイライト

  :hook (
    (prog-mode . display-fill-column-indicator-mode)  ;; 行長ガイド
  )

  :custom
  (display-line-numbers-type 'relative)    ;; 行番号を相対表示
  (show-paren-delay 0)
  (show-paren-style 'mixed)

  (fill-column 80)    // 行長ガイドを80に設定
)
```
