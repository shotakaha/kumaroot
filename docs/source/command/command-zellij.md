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

:::{note}

「ゼリージュ」はモロッコなどで見られる幾何学模様のモザイクタイルのことだそうです。

:::

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
| {kbd}`ctrl + g` | ロック操作 |
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

## ロック操作したい（`ctrl + g`）

`ctrl + g`で、zellijの操作キーをロック／アンロックできます。
いくつかの操作キーは、シェルの操作キーなどと重複しています。

たとえば`ctrl + p`と`ctrl + n`はコマンド履歴を遡るために使いますが、zellijではペイン操作とリサイズ操作に割り当てられています。
このような場合に`ctrl + g`で操作キーをロックすることで、シェルのほうにコマンドを送信できるようになります。

## ペイン操作したい（`ctrl + p`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + p` | {kbd}`n` | ペインを作成 |
| {kbd}`ctrl + p` | {kbd}`h` {kbd}`j` {kbd}`k` {kbd}`l` | ペインを移動 |
| {kbd}`ctrl + p` | {kbd}`←` {kbd}`↓` {kbd}`↑` {kbd}`→` | ペインを移動 |
| {kbd}`ctrl + p` | {kbd}`ENTER` | ペインを選択 |
| {kbd}`ctrl + p` | {kbd}`x` | ペインを閉じる |
| {kbd}`ctrl + p` | {kbd}`f` | フルスクリーン |
| {kbd}`ctrl + p` | {kbd}`w` | フローティングスクリーン |

## タブ操作したい（`ctrl + t`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + t` | {kbd}`n` | タブを作成 |
| {kbd}`ctrl + t` | {kbd}`h` {kbd}`l` | タブを移動 |
| {kbd}`ctrl + t` | {kbd}`←` {kbd}`→` | タブを移動 |
| {kbd}`ctrl + t` | {kbd}`ENTER` | タブを選択 |
| {kbd}`ctrl + t` | {kbd}`TAB` | タブをトグル |
| {kbd}`ctrl + t` | {kbd}`x` | タブを閉じる |

## リサイズ操作したい（`ctrl + n`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + n` | {kbd}`h` {kbd}`l` | ペインをリサイズ |

選択したペインのサイズを調整できます。
キーで入力した方向に拡大・縮小します。

## 移動操作（`ctrl + h`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + h` | {kbd}`h` {kbd}`l` | ペインを移動 |

選択したペインの表示位置を変更できます。
キーで入力した方向のペインと入れ替えます。

## 検索（`ctrl + s`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + s` | {kbd}`s` | ペイン内を検索 |
| {kbd}`ctrl + s` | {kbd}`↓` {kbd}`↑` | スクロール（1行） |
| {kbd}`ctrl + s` | {kbd}`d` {kbd}`u` | スクロール（半ページ） |
| {kbd}`ctrl + s` | {kbd}`e` {kbd}`u` | 編集 |

`less`コマンドのような操作ができます。

## セッション操作（`ctrl + o`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + o` | {kbd}`d` | セッションをデタッチ |
| {kbd}`ctrl + o` | {kbd}`w` | セッションを管理 |

作業を一時中断するときにデタッチしておけば、
アタッチして再開できます。

## セッションを再開したい（``attach``）

```console
// 既存のセッションを再開
$ zellij attach セッション名

// セッション名がなければ作成
$ zellij attach --create セッション名
```

`attach`コマンドで、セッションを再開できます。
`--create`オプションで、セッション名が存在しない場合に作成できます。

## セッションを確認したい（``list-sessions``）

```console
$ zellij list-sessions
kumaroot [Created 21m26m 59s ago] (current)
vitreous-apricot [Created 1m48s ago]
```

`list-sessions`コマンドで、セッション名を確認できます。
作業開始前に使うとよいでしょう。

:::{note}

シェルの起動スクリプトに追記してもよいかもしれません。

```fish
# ~/.config/fish/config.fish

if type -q zellij
    echo "=================================================="
    echo "Current Zellij Sessions:"
    zellij list-sessions
    echo "--------------------------------------------------"
    echo "Next:"
    echo "  Resume the session: 'zellij a SESSION_NAME'"
    echo "  Delete the session: 'zellij d SESSION_NAME'"
    echo "=================================================="
end
```

:::

```console
$ zellij list-sessions
vitreous-apricot [Created 12m 32s ago] (EXITED - attach to resurrect)
```

セッション名と一緒に、セッションの状態も確認できます。
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

## リファレンス

- [zellij](https://zellij.dev/)
- [zellij-org/zellij - GitHub](https://github.com/zellij-org/zellij)
