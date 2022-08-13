# 基本設定（``git config``）

[サルでも分かるGit入門 - Git設定](http://www.backlog.jp/git-guide/reference/config.html#sec1)を
一度は読むことをオススメします。
書いてあることが分からない場合はヘルプを見て確認するとよいです。

```bash
$ git config -h
```

## 設定済みの内容を確認したい

```bash
$ git config -l
```

## 基本項目を設定したい

ユーザー名やメールアドレス、使用するエディターなどは、あらかじめ設定しておきましょう。

```bash
$ git config --global user.name "Shota Takahashi"
$ git config --global user.email "shotakaha@gmail.com"
$ git config --global core.editor emacslient
```

``--global`` オプションをつけた場合は {file}`$HOME/.gitconfig` に書き込まれます。
このファイルに直接書き込んでもOKです。


## エイリアスを設定したい

各種コマンドのエイリアス（＝ショートカットキー）を設定できます。
この場合、たくさん設定することになるので、{command}`git config` を使うより、
{file}`$HOME/.gitconfig` に直接書き込んだ方が楽ちんです。

僕は以下のエイリアスを設定しています。
最初の4つはよくある設定で、 ``hist`` 以下の部分はどこかのサイトからのコピペです。
後述する ``Magit`` （EmacsのGitクライアント）を使い始めてから、コマンド操作することは減りました。

```unixconfig
[alias]
    co = checkout
    ci = commit
    st = status
    br = branch
    graph = log --graph --oneline
    hist = log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short
    type = cat-file -t
    dump = cat-file -p
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
    lga = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative --all
```
