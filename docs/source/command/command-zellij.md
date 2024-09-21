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
$ brew install --cask font-hack-nerd-font
```

`zellij`はHomebrewでインストールできます。
また、ナビゲーションを表示するためにNerd Font系が必要です。
`nerd`が含まれるフォントを追加し、ターミナルに設定してください。

:::{note}

僕はターミナル上のフォントを`Monaspace Krypton`に設定しています。
このフォントはNerd Fontに対応していないため
`--simplified-ui = true`に設定して使っています。

:::

## セッションしたい（`--session` / `-s`）

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
| {kbd}`ctrl + s` | ペイン内操作 |
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

## 移動操作したい（`ctrl + h`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + h` | {kbd}`h` {kbd}`l` | ペインを移動 |

選択したペインの表示位置を変更できます。
キーで入力した方向のペインと入れ替えます。

## ペイン内操作したい（`ctrl + s`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + s` | {kbd}`s` | ペイン内を検索 |
| {kbd}`ctrl + s` | {kbd}`↓` {kbd}`↑` | スクロール（1行） |
| {kbd}`ctrl + s` | {kbd}`d` {kbd}`u` | スクロール（半ページ） |
| {kbd}`ctrl + s` | {kbd}`e` {kbd}`u` | 編集 |

`less`コマンドのような操作ができます。

## セッション操作したい（`ctrl + o`）

| 操作キー | コマンド | 内容 |
|---|---|---|
| {kbd}`ctrl + o` | {kbd}`d` | セッションをデタッチ |
| {kbd}`ctrl + o` | {kbd}`w` | セッションを管理 |

作業を一時中断するときにデタッチしておけば、
アタッチして再開できます。

## セッションを再開したい（``attach`` / `a`）

```console
// 既存のセッションを再開
$ zellij attach セッション名
$ zellij a セッション名

// セッション名がなければ作成
$ zellij attach --create セッション名
```

`attach`コマンドで、セッションを再開できます。
`--create`オプションで、セッション名が存在しない場合に作成できます。

## セッションを確認したい（``list-sessions`` / `ls`）

```console
$ zellij list-sessions
$ zellij ls
kumaroot [Created 21m26m 59s ago] (current)
vitreous-apricot [Created 1m48s ago]
```

`list-sessions`コマンドで、セッション名を確認できます。
作業開始前に使うとよいでしょう。

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

## セッションを終了したい（``kill-session`` / `k`）

```console
$ zellij kill-session セッション名
$ zellij k セッション名

$ zellij kill-all-sessions セッション名
$ zellij ka セッション名
```

## セッションを削除したい（``delete-session`` / `d`）

```console
$ zellij delete-session セッション名
$ zellij d セッション名

$ zellij delete-all-sessions
$ zellij da
```

`delete-session`コマンドで、デタッチされたセッションを削除できます。
`delete-all-session`コマンドで、すべてのデタッチされたセッションを削除できます。

:::{note}

アクティブなセッションは削除されません。

:::

## 設定を確認したい（``setup --check``）

```console
// 設定を標準出力に表示
$ zellij setup --check
[Version]: "0.40.1"
[CONFIG DIR]: Not Found
[CONFIG FILE]: Not Found
[DATA DIR]: "~/Library/Application Support/org.Zellij-Contributors.Zellij"
[PLUGIN DIR]: "~/Library/Application Support/org.Zellij-Contributors.Zellij/plugins"
[LAYOUT DIR]: Not Found
[SYSTEM DATA DIR]: "/usr/share/zellij"
[ARROW SEPARATOR]: 
[MOUSE INTERACTION]:
[DEFAULT EDITOR]: Not set, checked $EDITOR and $VISUAL
[FEATURES]: []
[DOCUMENTATION]: https://www.zellij.dev/documentation/
```

``setup --check``で現在の設定を確認できます。

## キーバインドを設定したい

```console
// キーバインドを標準出力に表示
$ zellij setup --dump-config

// ファイルに保存
$ mkdir ~/.config/zellij
$ zellij setup --dump-config > ~/.config/zellij/config.kdl
```

`zellij`用の設定は`~/.config/zellij/`に保存します。
設定ファイルはKDL形式が採用されています。
設定できる内容は[Options](https://zellij.dev/documentation/options)で確認できます。

:::{note}

`0.32.0`以前はYAML形式だったようです。

:::

## コマンド補完したい

```console
// Fish用の補完を標準出力に表示
$ zellij setup --generate-completion fish

// ファイルに保存
$ zellij setup --generate-completion fish > ~/.config/fish/completions/zellij.fish
```

## 自動起動したい

```console
// Fish用の補完を標準出力に表示
$ zellij setup --generate-auto-start fish
```

自動で起動できるようのスクリプトがシェルごとに用意されています。

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

いつも自動起動だとセッションが溜まってしまいそうなので、
セッション名を確認できるようにだけしています。

## リファレンス

- [zellij](https://zellij.dev/)
- [zellij-org/zellij - GitHub](https://github.com/zellij-org/zellij)
