```{eval-rst}
.. index::
    pair: MyST; install
```

# インストールしたい（`mystmd`）

```console
// uv toolを使ってシステム全体にインストール
$ uv tool install mystmd

// uvを使ってプロジェクトに追加
$ uv add --group docs mystmd

$ myst --version
v1.3.25

$ which -a myst
/opt/homebrew/bin/myst
/Users/shotakaha/.local/bin/myst
```

MySTは`uv`でインストールできます。
パッケージ名は`mystmd`です。
インストールした後は、`myst`コマンドが使えるようになります。

:::{note}

[v1.1.0のリリース](https://github.com/executablebooks/mystmd/releases/tag/mystmd%401.1.0)で``myst-cli``から``mystmd``に名前が変わりました。

:::

:::{note}

[v1.1.7のリリース](https://github.com/executablebooks/mystmd/releases/tag/myst-cli%401.1.7)からPyPIにデプロイされるようになりました。
[pipx](../python/python-pipx.md)でもインストールできますが、Nodeのバージョンが合っていないと使えないみたいです。

:::
