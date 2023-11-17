```{eval-rst}
.. index::
    pair: MyST; install
```

## インストールしたい

```console
$ npm install -g mystmd

$ myst --version
v1.1.12

$ which myst
/opt/homebrew/bin/myst
```

``npm``を使って``mystmd``をインストールします。
とりあえずシステム全体にインストールしてOKです。

:::{note}

[v1.1.0のリリース](https://github.com/executablebooks/mystmd/releases/tag/mystmd%401.1.0)で``myst-cli``から``mystmd``に名前が変わりました。

:::

## インストールしたい（``pipx``）

```console
$ pipx install mystmd
Installing to existing venv 'mystmd'
  installed package mystmd 1.1.28, installed using Python 3.12.0
  These apps are now globally available
    - myst
done! ✨ 🌟 ✨

$ which myst
~/.local/bin/myst

$ myst --version
MyST requires node 16, 18, or 20; you are running node 21.
```

[v1.1.7のリリース](https://github.com/executablebooks/mystmd/releases/tag/myst-cli%401.1.7)からPyPIにデプロイされるようになりました。
[pipx](../python/python-pipx.md)でもインストールできますが、Nodeのバージョンが合っていないと使えないみたいです。

## アップデートしたい

```console
$ npm update -g mystmd
$ pipx upgrade mystmd
```
