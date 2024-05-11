# Gitクローンしたい（``ghq``）

```console
$ brew install ghq
$ ghq --version
ghq version 1.4.2 (rev:7163e61)


$ ghq get git@github.com:shotakaha/kumaroot.git
$ ghq get shotakaha/kumaroot
$ ghq get kumaroot

```

``ghq``は``git clone URL``を簡単にしてくれるコマンドです。
URLは、リポジトリからコピーしたフルパスに加えて、`ユーザー名リポジトリ名`も指定できます。
ユーザー名を省略した場合は、（おそらく）`ghq`コマンドを実行したユーザー名が適用されます。

## リポジトリをクローンしたい（``ghq get``）

```console
$ ghq get git@github.com:shotakaha/kumaroot.git
Cloning into '~/repos/github.com/shotakaha/kumaroot'...
```

``ghq get``コマンドで、``ghq.root``で設定したパスの下に、リポジトリのURLに沿った形式でクローンできるようになります。
どのディレクトリで実行してもOKなのも、このコマンドが便利な点です。

```console
$ ghq get shotakaha/kumaroot
    exists /Users/shotakaha/repos/github.com/shotakaha/kumaroot
```

すでにクローンしてあるプロジェクトを指定した場合は、
クローン済であることを教えてくれます。

## リポジトリを更新したい（``ghq get -u``）

```console
$ ghq get -u リポジトリ名
$ ghq get -u shotakaha/kumaroot
update ~/repos/github.com/shotakaha/kumaroot/
       git pull --ff-only
...
```

``-u, --update``オプションを使って、リポジトリを更新できます。
内部で``git pull --ff-only``しているようです。

## デフォルトディレクトリを設定したい

```console
$ git config --global ghq.root "~/repos/"
```

``git config``コマンドを使って``ghq.root``を変更できます。
デフォルトでは{file}`~/ghq`に設定されています。

:::{hint}

``ghq``コマンドは、僕の使い方にとてもマッチしていたツールでした。

このコマンドを知る以前は、同じようなことを手動でやっていました。

- Gitリポジトリはすべて{file}`~/repos/`の下で管理
- GitHubは{file}`~/repos/github/`の下にクローン
- GitLabは{file}`~/repos/gitlab/`の下にクローン
- 上記のクローンするパスは自分で指定

また、動作確認したいリポジトリは{file}`~/repos/sandbox/`の下にクローンして、いつでも使い捨てられるようにしているのですが、この使い方に並行して``ghq``コマンドを導入できました。

:::


## リポジトリを確認したい（``ghq list``）

```console
$ ghq list
github.com/Geant4/geant4
github.com/RedPitaya/RedPitaya
github.com/gohugoio/hugo
github.com/shotakaha/kumaroot
github.com/shotakaha/zenn-docs
github.com/typst/typst
gitlab.com/qumasan/haniwers
sandbox/getting-started
sandbox/hugo-quickstart
sandbox/hugo-sandbox
```

``ghq list``でクローンしたリポジトリのパスを表示できます。

:::{note}

``ghq``を使ってクローンしたかどうかに関係なく、``ghq.root``で指定したディレクトリにあるリポジトリがすべて表示されます。

:::

```console
$ ghq list 検索文字列

$ ghq list shotakaha
github.com/shotakaha/hugo_sandbox
github.com/shotakaha/kumaroot
github.com/shotakaha/zenn-docs
gitlab.com/shotakaha/brewfile
gitlab.com/shotakaha/cv
```

``ghq list``コマンドの引数に検索文字列を指定できます。
管理しているリポジトリが多い場合は、ユーザー名やプロジェクト名（の一部）で絞り込むことができます。
