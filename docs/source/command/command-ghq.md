# Gitクローンしたい（``ghq``）

```console
$ brew install ghq
$ ghq --version
ghq version 1.4.2 (rev:7163e61)
```

``ghq``は``git clone URL``を簡単にしてくれるコマンドです。

## デフォルトディレクトリを設定したい

```console
$ git config --global ghq.root "~/repos/"
```

``git config``コマンドを使って``ghq.root``を設定します。
デフォルトでは{file}`~/ghq`に設定されていますが、僕は{file}`~/repos/`に変更しました。

:::{hint}

もともと{file}`~/repos/`の下にクローンする形で管理していました。

GitHubは{file}`~/repos/github/`に、GitLabは{file}`~/repos/gitlab/`にというように、サービスごとにサブディレクトリを分けていました。
また、動作確認したいリポジトリは{file}`~/repos/sandbox/`の下にクローンして、使い捨てられるようにしていました。
なので``ghq``コマンドは、僕の使い方にとてもマッチしていたツールです。

:::

## リポジトリをクローンしたい（``ghq get``）

```console
$ ghq get git@github.com:shotakaha/kumaroot.git
Cloning into '~/repos/github.com/shotakaha/kumaroot'...
```

``ghq get``コマンドで、``ghq.root``で設定したパスの下に、リポジトリのURLに沿った形式でクローンできるようになります。
どのディレクトリで実行してもOKなのも、このコマンドが便利な点です。

## リポジトリを更新したい（``ghq get -u``）

```console
$ ghq get -u リポジトリ名
$ ghq get -u kumaroot
update ~/repos/github.com/shotakaha/kumaroot/
```

``-u, --update``オプションを使って、リポジトリを更新できます。

## リポジトリを確認したい（``ghq list``）

```console
$ ghq list
$ ghq list 検索文字列
$ ghq list | peco
```

``ghq list``でクローンしたリポジトリのパスを表示できます。
また、``peco``と組み合わせると絞り込み検索できます。
