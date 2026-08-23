```{eval-rst}
.. index::
    single: CLI; lsd
    single: List directory contents; lsd
    single: Rust Alternatives; lsd
```

# ファイル情報したい（`lsd`）

```console
$ lsd
$ lsd -l ファイル名
$ lsd -a
$ lsd -ltr
```

`lsd`は、ディレクトリの中身を一覧表示するコマンドです。
[ls](./command-ls.md)のRust代替コマンドです。

オプションは`ls`と同じですが、
表示結果にフォルダアイコンがついたり、色付けがされていたり、より見やすくなるように改善されています。

:::{note}

フォルダアイコンを表示するためには、ターミナル表示に使うフォントが、[Nerd Fonts](https://www.nerdfonts.com/)に対応している必要があります。

:::

:::{seealso}

- [](./command-ls.md)
- [](./command-exa.md)

:::

## インストールしたい（`lsd`）

```console
$ brew install lsd
$ lsd --version
lsd 1.2.0
```

`lsd`はHomebrewでインストールできます。

## 隠しファイルを表示したい（`lsd -a`）

```console
$ lsd -a
```

`-a`で、隠しファイルも含めたすべてのファイルを表示できます。
`.gitignore`や`.DS_Store`のように`.`ではじまるファイルは、ユーザー設定やシステム設定に関するファイルのため、通常の`lsd`では表示されないようになっています。

## 最新ファイルを確認したい（`lsd -ltr`）

```console
$ lsd -ltr
$ lsd -ltra
```

`-ltr`で、最近更新したファイルを確認できます。
`-t`は更新日時の新しい順に並べるオプション、
`-r`は逆順に並べるオプションです。
`-l`や`-a`は状況によって使い分けます。

一番新しいファイルが出力の末尾に表示されるので、
わざわざコマンドを実行した画面までスクロールする必要がなくなります。
