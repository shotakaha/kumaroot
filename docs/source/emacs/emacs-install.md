```{eval-rst}
.. index::
    pair: Emacs; install
```

# インストールしたい（`emacs`）

```console
// CLI: formula
$ brew install emacs

// GUI: Emacs.app
$ brew install --cask emacs-app
```

EmacsはHomebrewでインストールできます。
CLIだけでよい場合はフォーミュラ版（`emacs`）、
GUIを使う場合はCask版（`emacs-app`）を指定します。

:::{note}

以前は`emacs`という名前で、`formula`（CLIツール）と`cask`（GUIアプリ）の両方が提供されていました。
2025年6月にCaskのほうが`emacs-app`にリネームされました。

:::

GUI版は、Homebrewを使わずに
[Emacs for MacOSX](https://emacsformacosx.com)
からビルド済みのバイナリをダウンロードできます。
