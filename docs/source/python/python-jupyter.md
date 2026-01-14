# Jupyter Lab したい（`jupyter lab`）

```console
// jupyter-core から jupyter コマンドを読み込んで実行
$ uvx --from jupyter-core jupyter --version
Selected Jupyter core packages...
IPython          : not installed
ipykernel        : not installed
ipywidgets       : not installed
jupyter_client   : not installed
jupyter_core     : 5.9.1
jupyter_server   : not installed
jupyterlab       : not installed
nbclient         : not installed
nbconvert        : not installed
nbformat         : not installed
notebook         : not installed
qtconsole        : not installed
traitlets        : 5.14.3

// Jupyter Labを起動
$ uvx --from jupyter-core jupyter lab
```

`jupyter lab`コマンドでJupyter Labを起動できます。

:::{note}

`jupyter`自体はCLIパッケージではありません。
`uvx`を使って、隔離環境で実行する場合は`--from jupyter-core`を指定し、
`jupyter-core`パッケージから`jupyter`コマンドを読み込んで実行する必要があります。

:::

## インストールしたい（`jupyterlab` / `jupyter-core`）

- `uv`でインストール

```console
$ uv tool install jupyterlab
```

Jupyter関係のツールはサブパッケージに別れていますが、
`uv tool install`する場合`jupyterlab`パッケージを指定すればよさそうです。

- `uvx`で一時的にインストール

```console
$ uvx --from jupyter-core jupyter lab
```

`uvx`で一時的に`jupyter lab`を実行する場合は、
`jupyter-core`から`jupyter`コマンドをインストールします。

- `pipx`でインストール

```console
$ pipx install jupyter --include-deps
```

`pipx`の場合、``--include-deps``で関連パッケージをすべてインストールできます。

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

## VS Codeしたい

```console
$ uv pip install ipykernel
```

[Jupyter Extension for VS Code](https://github.com/Microsoft/vscode-jupyter)と
`ipykernel`をインストールすると、VS CodeでJupyter Labできます。
