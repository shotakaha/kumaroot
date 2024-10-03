# Jupyter Lab したい（``jupyter``）

```console
$ pipx install jupyter --include-deps
```

`pipx`でJupyter環境をインストールしました。
Jupyter関係のツールは、サブパッケージに分かれていますが、
``--include-deps``ですべてインストールできます。

## 拡張機能したい（`labextension`）

```console
// インストール済みの拡張機能を確認
$ jupyter labextension list

// 拡張機能のインストール
$ jupyter labextension install 拡張パッケージ名

// 拡張機能のアンインストール
$ jupyter labextension uninstall 拡張パッケージ名
```

`labextention`コマンドで、Jupyter Labの拡張機能を操作できます。

```console
$ jupyter labextension install @jupyterlab/extensionmanager
```

`@jupyterlab/extensionmanager`をインストールすると、
Jupyter Labのサイドバーに`Extension Manager`のタブが追加され、
GUIを使って拡張機能を追加できるようになります。

## キーバインド拡張したい

```console
// VS Code-likeなキーマップ
$ jupyter labextension install @jupyterlab/vscode-keymap

// Vim-likeなキーマップ
$ jupyter labextension install @axlair/jupyterlab_vim

// Emacs-likeなキーマップ
$ jupyter labextension install @jupyterlab/emacs-keymap
```
