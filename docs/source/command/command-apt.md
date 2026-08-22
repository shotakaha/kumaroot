# パッケージ管理したい（``apt``）

```console
$ apt
```

Debian系のLinuxでパッケージ管理を行うためのコマンドラインツールです。
昔は``apt-get``と``apt-cache``使っていた記憶がありますが、いまは``apt``を使うみたいです。

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
インストール済みパッケージは``dpkg -l``や``/var/lib/dpkg/status``で確認できます。

Dockerfileなどでは、``-y / --yes``や``--no-install-recommends``などのオプションをつけて使います。

## パッケージリストを更新したい（``apt update``）

```console
# apt-get update
$ apt update
```

``update``コマンドで、パッケージの更新を確認できます。
更新確認用のリストは``/etc/apt/sources.list.d/``（DEB822形式では``debian.sources``など）に保存されます。

:::{note}

``apt-get``は昔からあるコマンドで、``apt``は2016年ころに導入されたコマンド体系です。
できることはほぼ同じで、対話シェルでは``apt``の利用が推奨されています。
ただし、シェルスクリプトやDockerではまだ``apt-get``を使うほうがよいみたいです。

:::

## dpkgしたい（``dpkg``）

```console
$ dpkg -l
$ dpkg -l ripgrep
```

``apt``は、内部で``dpkg``というより低レベルなパッケージ管理コマンドを使っています。
``apt``がリポジトリからのダウンロードや依存関係の解決までまとめて面倒を見てくれるのに対して、
``dpkg``は手元にある``.deb``パッケージファイルを直接操作するコマンドです。

``-l``オプションで、インストール済みパッケージを一覧できます。
パッケージ名を指定すると、そのパッケージだけに絞り込めます。

```console
$ dpkg -L ripgrep
```

``-L``オプションで、指定したパッケージがインストールしたファイルの一覧を確認できます。

```console
$ dpkg -S /usr/bin/rg
```

``-S``オプションで、指定したファイルがどのパッケージによってインストールされたか調べられます。
``-L``の逆引きです。

```console
$ dpkg -s ripgrep
```

``-s``オプションで、パッケージの詳細情報（バージョン、依存関係、説明文など）を確認できます。

```console
$ apt-get download ripgrep
$ dpkg -i ripgrep_13.0.0-4+b2_arm64.deb
```

``-i``オプションで、``.deb``ファイルを直接インストールできます。
``apt``のリポジトリに登録されていない``.deb``ファイルを配布された場合に使います。

```console
$ dpkg -r ripgrep
```

``-r``オプションで、パッケージを削除できます。
設定ファイルは残るので、完全に削除したい場合は``apt purge``（もしくは``dpkg --purge``）を使います。

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
