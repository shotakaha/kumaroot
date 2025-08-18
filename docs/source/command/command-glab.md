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
$ glab issue list         # オープンなイシュー覧
$ glab issue list --all   # すべてのイシュー一覧（open/closed）
$ glab issue list --search "SEARCH_WARD"     # キーワード検索
$ glab issue list --label "bug,enhancement"  # ラベル検索

// イシューを表示
$ glab issue view <issue_id>                # イシューの詳細
$ glab issue view <issue_id> --web          # ブラウザで開く
$ glab issue note <issue_id> --message "comment"    # コメントを追加
$ glab issue note <issue_id>                # エディタを開く

// イシューを作成
$ glab issue create    # イシューを作成（interactive）
$ glab issue create --title "title" --description "desc"

// イシューを更新
$ glab issue update <id> --title "new title"
$ glab issue update <id> --description = "new desc"
$ glab issue update <id> --assignee @username
$ glab issue update <id> --label "bug,high"

// イシューの状態管理
$ glab issue close <id>
$ glab issue reopen <id>
$ glab issue delete <id>
$ glab issue subscribe <id>
$ glab issue unsubscribe <id>
```

`glab issue`でイシューを操作できます。
さらにサブコマンドを持ち、
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
$ glab mr list --all

// MRの詳細
$ glab mr view <mr_id>
$ glab mr view <mr_id> --web
$ glab mr note <mr_id> --message "comment"

// MRを作成
$ glab mr create
$ glab mr create --title "feat: add feature" --description "Close #123"
$ glab mr create --draft
$ glab mr create --target-branch develop

// MRの状態管理
$ glab mr approve <mr_id>
$ glab mr merge <mr_id>
$ glab close <mr_id>
$ glab reopen <mr_id>
$ glab revoke <mr_id>
$ glab delete <mr_id>
$ glab subscribe <mr_id>
$ glab unsubscribe <mr_id>
```

`glab mr`コマンドでマージリクエスト（MR）を操作できます。

`glab mr`でマージリクエスト（MR）を操作ができます。
さらにサブコマンドを持ち、
`list`でMRの一覧を取得し、
`view 番号`でMRの詳細を確認できます。
`create`で新しいMRを作成できます。

```console
// 作業ブランチに移動
$ git switch ブランチ名
$ glab mr create --draft --fill
```



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

## パイプラインしたい（`glab ci`）

```console
$ glab ci status
$ glab ci view --web
```

`glab ci`でパイプラインを操作できます。
