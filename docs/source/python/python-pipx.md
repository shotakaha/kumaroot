# パッケージ管理したい（``pipx``）

```console
$ pipx install パッケージ名
$ pipx upgrade パッケージ名
$ pipx uninstall パッケージ名
```

```console
$ brew install pipx
$ brew link pipx
$ pipx ensurepath
```

## シェル補完したい

```console
$ register-python-argcomplete --shell fish pipx >~/.config/fish/completions/pipx.fish
```

``pipx``コマンドのシェル補完が使えるようにすると便利です。
