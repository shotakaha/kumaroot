# インストールしたい（`quarto`）

```console
$ brew install --cask quarto

$ quarto --version
1.9.37
```

`quarto`は`Homebrew`でインストールできます。
インストールすると、`quarto`コマンドが使えるようになります。

```console
$ which -a quarto
/usr/local/bin/quarto
/Applications/quarto/bin/quarto
```

`quarto`コマンドは`/Applications/quarto/bin/quarto`です。
`/usr/local/bin/quarto`にシンボリックリンクが作成されているため、
なにも設定しなくても`quarto`コマンドが使えます。
