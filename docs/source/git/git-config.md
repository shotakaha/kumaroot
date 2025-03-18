# リポジトリ設定したい（`git config`）

```console
$ git config -h
```

`.gitconfig`にリポジトリ設定を記述できます。
ファイルを直接編集してもよいですが、基本的なアイテムは`git config`コマンドが便利です。

基本設定に関しては[サルでも分かるGit入門 - Git設定](https://backlog.com/ja/git-tutorial/reference/config/)を読むことをオススメします。
書いてあることが分からない場合はヘルプを見て確認するとよいです。

## 設定を確認したい（`--list`）

```console
$ git config -l
```

`-l / --list`オプションで現在の設定を確認できます。

## ユーザー設定したい（`--global`）

```console
$ git config --global user.name "Shota Takahashi"
$ git config --global user.email "shotakaha@gmail.com"
$ git config --global pull.rebase false
$ git config --global core.editor hx
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.co switch
$ git config --global alias.st status
```

`--global`オプションでユーザー設定できます。
ユーザー名（`user.name`）、
メールアドレス（`user.email`）、
デフォルトのマージ方法（`pull.rebase`）、
使用するエディター（`core.editor`）などは、
あらかじめ設定しておきましょう。
設定は`$HOME/.gitconfig` に保存されます。
このファイルに直接書き込んでもOKです。

## エディターを設定したい（`core.editor`）

```console
// Emacsに設定
$ git config --global core.editor emacslient

// VS Codeに設定
$ git config --global core.editor "code --wait"

// Helixに設定
$ git config --global core.editor hx
```

`core.editor`でコミットメッセージを編集するエディターを変更できます。
（使っているOSによるかもしれませんが）デフォルトでは`vim`が起動します。

Emacsのヘビーユーザーだったときは`emacsclinent`を使っていました。
いまはVS Codeを使っているため`code --wait`に設定しています。
[tig](../command/command-tig.md)を使う場合は`hx`（Helix）もいいかなと思います。

:::{note}

ターミナル内でEmacsを起動するだけなら`emacs -nw`でもできます。
しかし、**真のEmacsユーザー**であれば、基本的にEmacsは起動したままのはずです。
`emacsclient`は起動済みのEmacsに接続できるため、起動時の待ち時間を感じることなく
コミット作業が可能です。

:::

## エイリアスを設定したい（`alias`）

```console
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.co switch
$ git config --global alias.st status
```

`alias`でGitサブコマンドのエイリアス（＝ショートカットキー）を設定できます。
上記のサンプルは、よく使われている基本コマンドのエイリアスです。

```unixconfig
[alias]
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

エイリアスをまとめて設定する場合は、`git config` を使うより、
`$HOME/.gitconfig`を直接編集するほうが簡単です。

上記のサンプルは、僕が実際に設定しているエイリアスです。
`git graph`はコミットログを一覧で確認できて便利です。

:::{hint}

Git 2.23（2019年8月）に、`git checkout`コマンドが、
`git switch`と`git restore`の2つのコマンドに分離されました。
`switch`のエイリアスが`co`となっているのは`checkout`だったころの名残です。

:::

:::{note}

後述する
`Magit` （EmacsのGitクライアント）および
`EdaMagit`（MagitのVS Code移植版）を使い始めてから、
コマンド操作することは減りました。

:::

## マージ設定したい

```console
// mergeを使用
$ git config --global pull.rebase false

// rebaseを使用
$ git config --global pull.rebase true

// fast-forwardを使用
$ git config --global pull.ff only
```

`pull`で、リモートからプルしたときのマージ方法を設定できます。
基本は`pull.rebase false`でよいと思います。

:::{note}

Git2.27.0（2020年6月）以降、
マージ方法が設定されていないと警告が表示されるようになりました。

:::
