# ブランチを切り替えたい（``git checkout``）

```console
$ git checkout ブランチ名
```

``checkout``コマンドで、存在しているブランチに切り替えできます。
ブランチ名が存在しない場合は、メッセージが表示されて失敗します。

:::{seealso}

`checkout`は多機能すぎたため、Git 2.3.30からは役割を分割したコマンドが追加されました。

- [](./git-switch.md)
- [](./git-restore.md)

`checkout`コマンドは引き続き使用できますが、
ブランチ切り替えに限定した`switch`コマンドと
変更取り消しに限定した`restore`コマンドの使用が
推奨されています。

:::

## 新規ブランチしたい

```console
$ git checkout -b 新規ブランチ名 基準ブランチ名
```

``-b``オプションを使って、新しくブランチを作成してから切り替えできます。
基準ブランチ名を省略すると、現在のブランチになります。
基準ブランチ名の設定はクセにしておくとよいと思います。

## ファイルの変更を取り消したい

```console
$ git checkout -- ファイル名
```

ファイルの変更を取り消すこともできます。

## エイリアスしたい（``git co``）

```console
$ git config --global alias.co branch
```

[Git本](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-Git-%E3%82%A8%E3%82%A4%E3%83%AA%E3%82%A2%E3%82%B9)にあるように、``co``をエイリアスとして設定しておくと便利です。


