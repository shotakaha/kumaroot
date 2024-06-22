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

## ディレクトリにジャンプしたい（``z``）

```console
$ z ディレクトリ名（の一部）
$ z kumaroot
$ pwd
~/repos/github.com/shotakaha/kumaroot
```

``z ディレクトリ名``で、パスをすべて入力しなくても、ディレクトリにジャンプできます。

## 履歴からジャンプしたい（``zi``）

```console
$ zi
```

``zi``でよく使うディレクトリの履歴が表示されます。
ディレクトリ名（の一部）を入力して絞りこみ、カーソル移動で選択します。
