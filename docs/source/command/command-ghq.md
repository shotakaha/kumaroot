# Gitクローンしたい（``ghq``）

```console
$ brew install ghq
$ git config --global ghq.root "~/repos/"
```

``ghq``は``git clone URL``を簡単にしてくれるコマンドです。
僕はもともと、GitHubやGitLabから取得したソースは``~/repos/``に置くことにしていました。
このコマンドはそのような使い方ととてもマッチしています。

```console
$ ghq get git@github.com:shotakaha/kumaroot.git
Cloning into '~/repos/github.com/shotakaha/kumaroot'...
```

``ghq get``コマンドで、どのディレクトリにいても、``ghq.root``で設定したパスの下に、
リポジトリのURLに沿った形式でクローンできるようになります。
