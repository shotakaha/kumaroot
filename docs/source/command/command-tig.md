# Gitしたい（`tig`）

```console
$ tig
```

`tig`は、Gitの操作をターミナル上で視覚的に行えるTUIツールです。
`tig`と入力するだけで、Gitのコミット履歴を確認できます。
終了する場合は`q`を押します。
上下は矢印キー（{kbd}`↓` / {kbd}`↑`）の他に、vimのように{kbd}`j` / {kbd}`k`でも移動できます。
`RET`するとコミットの詳細が確認できます。

## インストールしたい（`tig`）

```console
$ brew install tig
$ tig --version
tig version 2.6.1
ncursesw version 6.6.20251230
readline version 8.3
PCRE2 version 10.47 2025-10-21
```

`tig`はHomebrewでインストールできます。

## あるブランチの履歴を確認したい

```console
$ tig ブランチ名
```

## ファイル／ディレクトリの履歴を確認したい

```console
$ tig ファイル1 ファイル2 ...
```

## 設定したい（`.tigrc`）

```console
#bind generic C !npx git-cz
bind generic C !git cz
```

{file}`~/.tigrc`で`tig`を設定できます。
ビューに表示する内容や、キーバインドなどを設定できます。

## ショートカットキー

| キー | Gitコマンド | 内容 |
|---|---|---|
| {kbd}`Q` | | tigを終了する |
| {kbd}`h` | | ショートカットキー一覧を表示する |
| {kbd}`m` | | メイン画面を表示する |
| {kbd}`r` | | ブランチ／タグなどを表示する |
| {kbd}`q` | | ひとつ前の画面に戻る |
| {kbd}`t` | | ディレクトリ構造を表示する |
| {kbd}`Enter` | | 選択した行の内容を表示する |
| {kbd}`s` | `git status` | ステータス画面を表示する |
| {kbd}`u` | `git add` / `git reset` | ステータス画面で選択したファイルをステージ / アンステージする |
| {kbd}`C` | `git commit` | コミットする |
| {kbd}`d` | `git diff` | カーソルを置いたコミットのdiff画面を表示する |
| {kbd}`l` | `git log` | コミットログを表示する |
| {kbd}`g` | `git grep` | リポジトリ内を検索する |
