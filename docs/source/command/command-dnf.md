# パッケージ管理したい（`dnf`）

```console
$ dnf install epel-release
$ dnf search パッケージ名
$ dnf install パッケージ名
$ dnf check-update
$ dnf upgrade
```

`dnf`はRHEL系OS（RHEL / Rocky Linux / AlmaLinux / CentOS Stream / Fedora）のパッケージ管理コマンドです。
`yum`の後継で、依存関係の解決やパフォーマンスなどが改善されています。

## パッケージを検索したい（`dnf search`）

```console
$ dnf search パッケージ名
$ dnf search vim
```

`dnf search`で、パッケージ名や概要にキーワードが含まれるパッケージを検索できます。

## パッケージの詳細を調べたい（`dnf info`）

```console
$ dnf info パッケージ名
$ dnf info vim-enhanced
```

`dnf info`で、パッケージのバージョンやサイズ、説明などの詳細情報を確認できます。

## パッケージをインストールしたい（`dnf install`）

```console
$ dnf install パッケージ名
$ dnf install vim-enhanced
```

`dnf install`でパッケージをインストールできます。
複数のパッケージ名を一度に指定できます。
インストール済みパッケージは`dnf list installed`や`rpm -qa`で確認できます。

Dockerfileなどでは、`-y`オプションをつけて確認プロンプトを省略します。

## パッケージを削除したい（`dnf remove`）

```console
$ dnf remove パッケージ名
$ dnf remove vim-enhanced
```

`dnf remove`で、インストール済みのパッケージを削除できます。

## パッケージを更新したい（`dnf upgrade`）

```console
$ dnf check-update
$ dnf upgrade
```

`dnf check-update`で、更新可能なパッケージを一覧できます。
`dnf upgrade`で、更新可能なパッケージをすべて更新します。
`dnf upgrade パッケージ名`で、指定したパッケージだけを更新することもできます。

## 不要なファイルを削除したい（`dnf clean`）

```console
$ dnf clean packages
$ dnf clean all
```

`dnf clean`で、ダウンロード済みのパッケージファイルやメタデータのキャッシュを削除できます。
`packages`はダウンロード済みの`.rpm`ファイルのみ、`all`はメタデータも含めてすべて削除します。

## 操作履歴を確認したい（`dnf history`）

```console
$ dnf history
```

`dnf history`で、`dnf`コマンドの実行履歴（インストール・削除・更新の記録）を確認できます。

## rpmしたい（`rpm`）

```console
$ rpm -qa
$ rpm -qa | grep パッケージ名
```

`rpm`は、RHEL系Linuxのパッケージ管理の低レベルコマンドです。
`dnf`も内部で`rpm`を使っています。

手元にある`.rpm`パッケージファイルを直接操作するコマンドです。
日常的に使うことはほぼありませんが、トラブルシュートしたいときに覚えておくとよいかもしれません。

`-qa`オプションで、インストール済みパッケージを一覧できます。

```console
$ rpm -ql vim-enhanced
```

`-ql`オプションで、指定したパッケージがインストールしたファイルの一覧を確認できます。

```console
$ rpm -qf /usr/bin/vim
```

`-qf`オプションで、指定したファイルがどのパッケージによってインストールされたか調べられます。
`-ql`の逆引きです。

```console
$ rpm -qi vim-enhanced
```

`-qi`オプションで、パッケージの詳細情報（バージョン、依存関係、説明文など）を確認できます。

```console
$ dnf install --downloadonly --downloaddir=. パッケージ名
$ rpm -i パッケージ名.rpm
```

`-i`オプションで、`.rpm`ファイルを直接インストールできます。
`dnf`のリポジトリに登録されていない`.rpm`ファイルを配布された場合に使います。

```console
$ rpm -e パッケージ名
```

`-e`オプションで、パッケージを削除できます。

## リポジトリを追加したい

```console
$ dnf install epel-release
$ dnf repolist
```

`epel-release`は、
EPEL（Extra Packages for Enterprise Linux）という、標準リポジトリを拡張するパッケージです。
他にも、主要な拡張リポジトリは`〇〇-release`という名前で提供されています。
標準リポジトリにないパッケージを使いたい場合は、まず追加しておくとよいです。

```console
$ dnf install 'dnf-command(config-manager)'
$ dnf config-manager --add-repo リポジトリのURL
```

`〇〇-release`パッケージが提供されていない場合、`config-manager`コマンドで`.repo`ファイルを直接追加する必要があります。
`config-manager`もデフォルトでは入っていないプラグインなので、`dnf install 'dnf-command(config-manager)'`で、先にインストールが必要です。

:::{note}

RHEL系はエンタープライズ向けの思想が強く、標準リポジトリに含まれるパッケージが絞られています。
その代わり、EPELのような拡張リポジトリを`〇〇-release`パッケージとして手軽に追加できるように整備されています。

:::

## リファレンス

- [DNF Command Reference](https://dnf.readthedocs.io/en/latest/command_ref.html)
- [RPM Documentation](https://rpm.org/docs/)
