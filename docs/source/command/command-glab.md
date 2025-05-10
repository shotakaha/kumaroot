# GitLabしたい（`glab`）

```console
// イシューの確認
$ glab issue list
$ glab issue view issue番号

// ブランチを作成
$ glab issue checkout issue番号

// MRドラフトを作成
$ glab mr create --draft --fill
$ glab mr view --web
```

`glab`でGitLabリポジトリを操作できます。
プロジェクトの`.git/config`から自動でリポジトリを判別して、操作対象にしてくれます。

## インストールしたい

```console
$ brew install glab
```

## ログインしたい（`glab auth`）

```console
// ログイン
$ glab auth login

// ログアウト
$ glab auth logout

// 確認
$ glab auth status
```

はじめて使う場合は、認証が必要です。
GitLabホスト、使用するGitプロトコル（SSH/HTTPS/HTTP）、
認証方法の選択（ウェブブラウザ／PAT）などをターミナル上で対話的に選択します。

設定した内容は`~/.config/glab-cli/config.yml`に保存されます。

## イシューしたい（`glab issue`）

```console
// イシューを確認
$ glab issue list
$ glab issue view --web イシュー番号

// イシューを作成
$ glab issue create --web --title タイトル
```

`glab issue`でイシューに関する操作ができます。
`list`でイシューの一覧を取得し、
`view 番号`でイシューの詳細を確認できます。
`create`で新しいイシューを作成できます。

:::{tip}

`view`と`create`は`--web`オプションでブラウザが開きます。
ターミナルより、ブラウザのほうが確認しやすいと思います。

:::

## マージリクエストしたい（`glab mr`）

```console
// MRを確認
$ glab mr list
$ glab mr view 番号 or ブランチ名

// 作業ブランチに移動
$ git switch ブランチ名
$ glab mr create --draft --fill
```

`glab mr`でマージリクエスト（MR）を操作できます。

`git switch`で作業ブランチに移動し、`glab mr create`で新しいMRを作成できます。
`--draft`オプションでMRドラフトを作成できます。
`--fill`オプションでコミットメッセージからタイトルと本文を自動入力してくれます。

```console
$ git add ファイル名
$ git commit
$ git fetch origin
$ git merge origin/main  # or git rebase origin/main
$ git push  # or git push -u origin ブランチ名
```

ローカルにあるリポジトリの操作は、いつも通り`git`を使います。

## マージしたい

```console
// MRを承認（オプション）
$ glab mr approve MR番号

// MRをマージ
$ glab mr merge MR番号
```

## パイプラインしたい（`glab ci`）

```console
$ glab ci status
$ glab ci view --web
```

`glab ci`でパイプラインを操作できます。
