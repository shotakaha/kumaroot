```{eval-rst}
.. index::
    single: CLI; zoxide
    single: 移動したい; zoxide
    single: Rust Alternatives; zoxide
```

# ディレクトリ移動したい（``zoxide``）

```console
$ brew install zoxide
```

## シェルごとの初期設定したい（``init``）

```console
$ zoxide init シェル名
$ zoxide init fish
// To initialize zoxide, add this to your configuration
// (usually ~/.config/fish/config.fish):
//
//  zoxide init fish | source
```

シェルごとに``zoxide``の初期設定コマンドが用意されています。
表示された内容の末尾に、設定方法が書いてあるので、それに従います。

## ディレクトリを移動したい（``zi``）

```console
$ zi
```

``zi``でよく使うディレクトリの一覧が表示されます。
移動したいディレクトリをカーソルで選択します。
