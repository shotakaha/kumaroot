```{tags} raspi, apt
```

# パッケージ管理したい（``apt``）

```console
$ sudo apt update
$ sudo apt full-upgrade
```

初回起動したあとは``apt full-upgrade``します。

```console
$ sudo apt update
$ sudo apt upgrade
```

定期的に更新する場合は``apt upgrade``します。

## パッケージを探したい（``apt-cache search``）

```console
$ apt-cache search パッケージ名
```

## パッケージを追加したい（``apt install``）

```console
$ sudo apt install ripgrep
$ sudo apt install bat
$ sudo apt install fd-find
$ sudo apt install lsd
$ sudo apt install tealdeer
$ sudo apt install fish
$ sudo apt install vim
$ sudo apt install code
$ sudo apt install python3-pip python3-venv pipx
$ sudo apt install openssh-server
```

よく使うパッケージを追加しました。
``ripgrep``から``lsd``までは、Rust代替コマンドです。
``tealdeer``はmanコマンドの簡単バージョンです。
``fish``シェルをデフォルトシェルとして使います
Pythonの仮想環境は``poetry``を使って整えます。
