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
```

ユーザー名やメールアドレス、使用するエディターなどは、あらかじめ設定しておきましょう。
``--global`` オプションをつけた場合は {file}`$HOME/.gitconfig` に書き込まれます。
このファイルに直接書き込んでもOKです。

## エディターを設定したい

```console
$ git config --global core.editor emacslient
$ git config --global core.editor "code --wait"
$ git config --global core.editor hx
```

``git commit``したときに起動するエディターを変更できます。
（使っているOSによるかもしれませんが）デフォルトでは``vim``が起動します。

Emacsヘビーユーザーだったころは``emacsclinent``に変更していました。
VS Codeユーザーのいまは``code --wait``に変更しています。
``tig``をメインで使う場合、``hx``（Helix）もいいかなと思います。

:::{note}

Emacsをターミナル内で起動する場合は``emacs -nw``でもできます。
しかし、（真の）Emacsユーザーは、基本的にEmacsを起動したままにしているはずです。
その場合は``emacsclient``を使うのが最適解です。

:::

## エイリアスを設定したい

```unixconfig
[alias]
    # co = checkout
    co = switch
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
