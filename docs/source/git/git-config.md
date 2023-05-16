# 基本設定したい（``git config``）

```console
$ git config -h
```

[サルでも分かるGit入門 - Git設定](https://backlog.com/ja/git-tutorial/reference/config/)を
一度は読むことをオススメします。
書いてあることが分からない場合はヘルプを見て確認するとよいです。

## 設定済みの内容を確認したい

```console
$ git config -l
```

## 基本項目を設定したい

```console
$ git config --global user.name "Shota Takahashi"
$ git config --global user.email "shotakaha@gmail.com"
$ git config --global pull.rebase false
$ git config --global core.editor emacslient
```

ユーザー名やメールアドレス、使用するエディターなどは、あらかじめ設定しておきましょう。
``--global`` オプションをつけると {file}`$HOME/.gitconfig` に設定が保存されます。
このファイルを直接編集してもOKです。

## エイリアスを設定したい

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

よく使うGitサブコマンドはエイリアス（＝ショートカットキー）を設定しておくとよいです。
一度にたくさんのエイリアス設定する場合は、{command}`git config` を使うより、
{file}`$HOME/.gitconfig` に直接書き込んだ方が楽ちんです。

僕が設定しているエイリアスを載せておきました。
最初の4つはよくある設定で、 ``hist`` 以下の部分はどこかのサイトからのコピペです。
後述する ``Magit`` （EmacsのGitクライアント）を使い始めてから、コマンド操作することは減りました。
