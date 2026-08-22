# パッケージ管理したい（`apt`）

```console
$ apt
```

`apt`は、`.deb`形式のパッケージを管理するコマンドです。
Debian系のLinuxで利用されます。

`apt-get`と`apt-cache`の機能を統合したコマンドで、対話シェルでの利用が推奨されています。

:::{note}

CI/CDやDockerfileなど、対話的でないシェルスクリプトでは、まだ`apt-get`や`apt-cache`を使うほうがよいみたいです。

:::

## パッケージを検索したい（`apt search`）

```console
$ apt search パッケージ名
$ apt search ripgrep

# apt-cache search パッケージ名
```

`apt search`で、指定したパッケージ名を検索できます。

## パッケージをインストールしたい（`apt install`）

```console
$ apt install パッケージ名
$ apt install ripgrep

# apt-get install パッケージ名
$ apt-get install -y --no-install-recommends git    // Dockerfile
```

`apt install`で、パッケージをインストールできます。
複数のパッケージ名を一度に指定できます。
インストール済みパッケージは`dpkg -l`や`/var/lib/dpkg/status`で確認できます。

Dockerfileなどでは、`-y / --yes`や`--no-install-recommends`などのオプションをつけて使います。

## パッケージリストを更新したい（`apt update`）

```console
$ apt update

# apt-get update
```

`apt update`で、パッケージの更新を確認できます。
更新確認用のリストは`/etc/apt/sources.list.d/`（DEB822形式では`debian.sources`など）に保存されます。

## aptitudeしたい（`aptitude`）

```console
$ apt install aptitude
$ aptitude --version
aptitude 0.8.13
```

`aptitude`は、`apt`とは別系統の高機能なパッケージ管理コマンドです。
デフォルトではインストールされていないので、使いたい場合は別途インストールします。

引数なしで実行すると`ncurses`ベースの画面が起動します。
矢印キーでパッケージを選んでインストール・削除できます。
依存関係の解決アルゴリズムも`apt`より賢いと言われています。

```console
$ aptitude search ripgrep
p  ripgrep - Recursively searches directories for a regex pattern

$ aptitude install ripgrep
$ aptitude show ripgrep
```

`search`、`install`、`show`などのサブコマンドも利用できます。
サブコマンドは`apt`とほぼ同じ感覚で使えます。

## dpkgしたい（`dpkg`）

```console
$ dpkg -l
$ dpkg -l ripgrep
```

`dpkg`は、Debian系Linuxのパッケージ管理の低レベルコマンドです。
`apt`も内部で`dpkg`を使っています。

手元にある`.deb`パッケージファイルを直接操作するコマンドです。
日常的に使うことはほぼありませんが、トラブルシュートしたいときに覚えておくとよいかもしれません。

`-l`オプションで、インストール済みパッケージを一覧できます。
パッケージ名を指定すると、そのパッケージだけに絞り込めます。

```console
$ dpkg -L ripgrep
```

`-L`オプションで、指定したパッケージがインストールしたファイルの一覧を確認できます。

```console
$ dpkg -S /usr/bin/rg
```

`-S`オプションで、指定したファイルがどのパッケージによってインストールされたか調べられます。
`-L`の逆引きです。

```console
$ dpkg -s ripgrep
```

`-s`オプションで、パッケージの詳細情報（バージョン、依存関係、説明文など）を確認できます。

```console
$ apt-get download ripgrep
$ dpkg -i ripgrep_13.0.0-4+b2_arm64.deb
```

`-i`オプションで、`.deb`ファイルを直接インストールできます。
`apt`のリポジトリに登録されていない`.deb`ファイルを配布された場合に使います。

```console
$ dpkg -r ripgrep
```

`-r`オプションで、パッケージを削除できます。
設定ファイルは残るので、完全に削除したい場合は`apt purge`（もしくは`dpkg --purge`）を使います。

## リポジトリを追加したい

```console
$ install -m 0755 -d /etc/apt/keyrings
$ curl -fsSL リポジトリのGPG鍵のURL -o /etc/apt/keyrings/リポジトリ名.asc
```

標準リポジトリにないパッケージを使いたい場合は、リポジトリを追加します。
まず、リポジトリが提供するGPG鍵をダウンロードして`/etc/apt/keyrings/`に保存します。

```console
$ echo 'deb [arch=アーキテクチャ signed-by=/etc/apt/keyrings/リポジトリ名.asc] リポジトリのURL コードネーム stable' > /etc/apt/sources.list.d/リポジトリ名.list

$ apt update
```

`/etc/apt/sources.list.d/`に`.list`ファイルを追加し、`signed-by`で先ほどのGPG鍵を紐付けます。
`apt update`を実行すると、追加したリポジトリのパッケージも検索・インストールできるようになります。

:::{note}

以前は`apt-key`コマンドでGPG鍵を登録する方法が主流でしたが、非推奨になりました。
GPG鍵をファイルとして`/etc/apt/keyrings/`に保存し、`sources.list`（または`.list`ファイル）側で`signed-by`を指定する方法が現在推奨されています。

:::

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
