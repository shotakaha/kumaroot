```{eval-rst}
.. index::
    single: CLI; zoxide
    single: 移動したい; zoxide
    single: Rust Alternatives; zoxide
```

# ディレクトリ移動したい（`zoxide`）

```console
// ディレクトリを指定
$ z ディレクトリ名（の一部）

// 履歴から選択
$ zi
```

`zoxide`は、ディレクトリ移動を便利にするコマンドです。
`z`コマンドで、パスをすべて入力しなくても、ディレクトリにジャンプできます。
`zi`コマンドで、よく使うディレクトリの履歴から選択してジャンプできます。

## インストールしたい（`zoxide`）

```console
$ brew install zoxide
$ zoxide --version
zoxide 0.10.0
```

`zoxide`はHomebrewでインストールできます。

## シェルごとの初期設定したい（`zoxide init`）

```console
$ zoxide init シェル名
$ zoxide init fish
// To initialize zoxide, add this to your configuration
// (usually ~/.config/fish/config.fish):
//
//  zoxide init fish | source
```

`zoxide init`で、初期設定コマンドを表示できます。
初期設定コマンドは、シェルごとに用意されています。
表示内容の末尾に、設定方法が書いてあるので、それに従います。

## ディレクトリにジャンプしたい（`z`）

```console
$ z ディレクトリ名（の一部）
$ z kumaroot
$ pwd
~/repos/github.com/shotakaha/kumaroot
```

`z ディレクトリ名`で、パスをすべて入力しなくても、ディレクトリにジャンプできます。

## 履歴からジャンプしたい（`zi`）

```console
$ zi
```

`zi`でよく使うディレクトリの履歴が表示されます。
ディレクトリ名（の一部）を入力して絞りこみ、カーソル移動で選択します。

## リファレンス

- [zoxide - GitHub](https://github.com/ajeetdsouza/zoxide)
