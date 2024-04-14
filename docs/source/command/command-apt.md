# パッケージ管理したい（``apt``）

```console
$ apt
```

Debian系のLinuxでパッケージ管理を行うためのコマンドラインツールです。
昔は``apt-get``と``apt-cache``使っていた記憶がありますが、いまは``apt``を使うみたいです。

## パッケージリストを更新したい（``apt update``）

```console
# apt-get update
$ apt update
```

``update``コマンドで、パッケージの更新を確認できます。
更新確認用のリストは``/etc/apt/sources.list``に保存されます。

:::{note}

``apt-get``は昔からあるコマンドで、``apt``は2016年ころに導入されたコマンド体系です。
できることはほぼ同じで、対話シェルでは``apt``の利用が推奨されています。
ただし、シェルスクリプトやDockerではまだ``apt-get``を使うほうがよいみたいです。

:::

## パッケージを検索したい（``apt search``）

```console
# apt-cache search パッケージ名
$ apt search パッケージ名
$ apt search ripgrep
```

## パッケージをインストールしたい（``apt install``）

```console
# apt-get install パッケージ名
$ apt install パッケージ名

$ apt install ripgrep
$ apt-get install -y --no-install-recommends git    // Dockerfile
```

``install``コマンドでパッケージをインストールできます。
複数のパッケージ名を一度に指定できます。
インストールされたパッケージは``/var/lib/apt/lists/``で確認できます。

Dockerfileなどでは、``-y / --yes``や``--no-install-recommends``などのオプションをつけて使います。

## オススメのパッケージ

```console
$ apt install build-essential
$ apt install gdb
$ apt install vim
$ apt install git
$ apt install openssh-client
$ apt install libssl-dev libpq-dev
$ apt install docker.io
$ apt install python3
$ apt install python3-pip
$ apt install nodejs
$ apt install ruby
$ apt install ripgrep
```

## リファレンス

- [apt - manpages.ubuntu.com](https://manpages.ubuntu.com/manpages/noble/en/man8/apt.8.html)
- [apt-get - manages.ubuntu.com](https://manpages.ubuntu.com/manpages/noble/en/man8/apt-get.8.html)
