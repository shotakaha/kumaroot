# ブランチしたい（``git branch``）

```console
$ git branch
  fix-git-branch
* main

$ git branch -a
  fix-git-branch
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/fix-git-branch
  remotes/origin/main
```

``git branch``で、ローカルにあるブランチ名を確認できます。
``*``がついているのが、現在の作業ブランチです。
``-a``オプションで、リモート（``/remotes/origin/``）も含めたすべてのブランチを確認できます。

## エイリアスしたい（``git br``）

```console
$ git config --global alias.br branch
```

[Git本](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-Git-%E3%82%A8%E3%82%A4%E3%83%AA%E3%82%A2%E3%82%B9)にあるように、``br``をエイリアスとして設定しておくと便利です。

## ブランチを作成したい

```console
$ git branch ブランチ名
```

現在の作業ブランチから、新しくブランチを作成できます。
ベースにするブランチ名が正しいか、必ず確認しましょう。
すでに存在する名前のブランチ名を指定すると、メッセージが表示されて失敗します。

## ブランチを削除したい

```console
$ git branch -d ブランチ名
$ git branch -D ブランチ名  # 強制削除
```

``-d ブランチ名``オプションで、指定したブランチを削除できます。
削除指定したブランチでの作業がまだマージされてない場合は、メッセージが表示されて失敗します。
``-D ブランチ名``オプションで強制削除できます。

## マージされたか確認したい

```console
// マージ済みのブランチを表示
$ git branch --merged

// マージされてないブランチを表示
$ git branch --no-merged
```

`--merged`オプションで、マージ済みのブランチかどうかを確認できます。
ローカルブランチの数を整理したい場合に使います。
