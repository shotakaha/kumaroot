# ターミナル管理したい（`zellij`）

```console
$ zellij --help
$ zellij --session セッション名
$ zellij list-sessions
$ zellij attach セッション名
$ zellij delete-session セッション名
```

`zellij`（ゼリージュ）はターミナルマルチプレクサーという
ターミナル管理（？）ツールです。
ターミナルの中にターミナル（＝セッションと呼ぶ）を
入れ子にできるようになっているので、
作業に必要なディレクトリ／ファイルを表示・整理できます。

また、リモートサーバーで`zellij`セッションを作成してプロセスを走らせておくと、クライアントからの接続を閉じても再接続後に再開できます。

## インストールしたい（``zellij``）

```console
$ brew install zellij
```

## セッションしたい（`-s` / `--session`）

```console
$ zellij

// セッション名を指定する
$ zellij -s セッション名
```

`zellij`コマンドでセッションを作成できます。
`--session`オプションでセッション名を指定できます。

## セッション操作したい（`Ctrl + キー`）

| 操作キー | 内容 |
|---|---|
| {kbd}`ctrl + g` | ロック |
| {kbd}`ctrl + p` | ペイン操作 |
| {kbd}`ctrl + t` | タブ操作 |
| {kbd}`ctrl + r` | リサイズ操作 |
| {kbd}`ctrl + h` | 移動操作 |
| {kbd}`ctrl + s` | 検索 |
| {kbd}`ctrl + o` | セッション操作 |
| {kbd}`ctrl + q` | 終了 |

セッション内は{kbd}`ctrl + キー`で操作を開始できます。
この操作キーは、画面の下部に表示されているため、事前に覚える必要はありません。
また、トグルになっているため、間違えて押してしまった場合でも同じキーで取り消せるので便利です。

:::{caution}

`ctrl + p`と`ctrl + n`はコマンド履歴を遡るために使うので、操作キーに使われている点は不便だと感じました。
プレフィックスキーを`control`から`command`に置き換えたかったのですが、無理みたいでした。

:::

## セッションを確認したい（``list-sessions``）

```console
$ zellij list-sessions
kumaroot [Created 21m26m 59s ago] (current)
vitreous-apricot [Created 1m48s ago]
```

`list-sessions`コマンドで、既存のセッション名を確認できます。

```console
$ zellij list-sessions
vitreous-apricot [Created 12m 32s ago] (EXITED - attach to resurrect)
```

終了したセッションは`EXITED`と表示されます。

```console
$ zellij list-sessions
No active zellij sessions found.
```

セッションがない場合は
`No active zellij sessions found.`
と表示されます。

## セッションを削除したい（``delete-session``）

```console
$ zellij delete-session セッション名
$ zellij delete-all-sessions
```

`delete-session`コマンドで、デタッチされたセッションを削除できます。
`delete-all-session`コマンドで、すべてのデタッチされたセッションを削除できます。

:::{note}

アクティブなセッションは削除されません。

:::
