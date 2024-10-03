# Jupyter Lab したい（``jupyter``）

```console
$ jupyter --version
jupyter --version
Selected Jupyter core packages...
IPython          : not installed
ipykernel        : not installed
ipywidgets       : not installed
jupyter_client   : not installed
jupyter_core     : 5.7.2
jupyter_server   : not installed
jupyterlab       : not installed
nbclient         : not installed
nbconvert        : not installed
nbformat         : not installed
notebook         : not installed
qtconsole        : not installed
traitlets        : 5.14.3

// Jupyter Notebookを起動
$ jupyter notebook

// Jupyter Labを起動
$ jupyter lab
```

## インストールしたい（`jupyter`）

- `pipx`でインストール

```console
$ pipx install jupyter --include-deps
```

- `uv`でインストール

```console
$ uv tool install jupyter-core
# - jupyter
# - jupyter-migrate
# - jupyter-troubleshoot

$ uv tool install jupyterlab
# - jlpm
# - jupyter-lab
# - jupyter-labextension
# - jupyter-labhub

$ uv tool install notebook
# - jupyter-notebook

$ uv tool install jupyter-server
# - jupyter-server

$ uv tool install jupyter-client
# - jupyter-kernel
# - jupyter-kernelspec
# - jupyter-run

$ uv tool install jupyter-events
# - jupyter-events

$ uv tool install jsonschema
# - jsonschema

$ uv tool install jsonpointer
# - jsonpointer

$ uv tool install nbconvert
# - jupyter-dejavu
# - jupyter-nbconvert

$ uv tool install nbclient
# - jupyter-execute

$ uv tool install nbformat
# - jupyter-trust

$ uv tool install pygments
# - pygmentize

$ uv tool install send2trash
# - send2trash

$ uv tool install websocket-client
# - wsdump

$ uv tool install babel
# - pybabel

$ uv tool install json5
# - pyjson5

$ uv tool install charset-normalizer
# - normalizer

$ uv tool install httpx
# - httpx

$ uv tool install debugpy
# - debugpy

$ uv tool install ipython
# - ipython
# - ipython3

$ uv tool install jupyter-console
# - jupyter-console
```

Jupyter関係のツールは、サブパッケージに分かれていますが、
`pipx`の場合、``--include-deps``ですべてインストールできます。

:::{note}

`uv`はそれぞれインストールする必要がありました。
どれが必要かわからないので、とりあえずすべて追加しました。
一括アップデートのコマンドもないので、更新も大変そう・・・。

:::

## 拡張機能したい（`labextension`）

```console
// インストール済みの拡張機能を確認
$ jupyter labextension list
JupyterLab v4.2.5
~/.local/share/uv/tools/jupyterlab/share/jupyter/labextensions
    jupyterlab_pygments v0.3.0 enabled OK (python, jupyterlab_pygments)

// 拡張機能のインストール
$ jupyter labextension install 拡張パッケージ名

// 拡張機能のアンインストール
$ jupyter labextension uninstall 拡張パッケージ名
```

`labextention`コマンドで、Jupyter Labの拡張機能を操作できます。

:::{caution}

> (Deprecated) Uninstalling extensions with the jupyter labextension uninstall command is now deprecated and will be removed in a future major version of JupyterLab.
>
> Users should manage prebuilt extensions with package managers like pip and conda, and extension authors are encouraged to distribute their extensions as prebuilt packages

`labextension`コマンドでインストール、アンインストールする方法は非推奨だそうです。

:::

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
