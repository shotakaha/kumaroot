# ブランチを切り替えたい（``git checkout``）

```console
$ git checkout ブランチ名
```

``checkout``コマンドで、存在しているブランチに切り替えできます。
ブランチ名が存在しない場合は、メッセージが表示されて失敗します。

## エイリアスしたい（``git co``）

```console
$ git config --global alias.co branch
```

[Git本](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-Git-%E3%82%A8%E3%82%A4%E3%83%AA%E3%82%A2%E3%82%B9)にあるように、``co``をエイリアスとして設定しておくと便利です。

## 新規ブランチしたい

```console
$ git checkout -b 新規ブランチ名 基準ブランチ名
```

``-b``オプションを使って、新しくブランチを作成してから切り替えできます。
基準ブランチ名を省略すると、現在のブランチになります。
基準ブランチ名の設定はクセにしておくとよいと思います。
