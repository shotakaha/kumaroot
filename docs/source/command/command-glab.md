# GitLabしたい（`glab`）

```console
// ログイン
$ glab auth login

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

`glab`をはじめて使う場合は、認証が必要です。
認証には、ウェブ認証とトークン認証があります。

ちょっと使いたい場合はウェブ認証、
しっかり使いたい場合はトークン認証で設定するとよいです。

:::{note}

トークン認証にはGitLab上でPAT（Personal Access Token）を作成する必要があります。
トークンはページ上に1度しか表示されません。
もし、コピーに失敗した場合は、そのトークンを削除して、新しいトークンを作成してください。

トークンは「目的ごと」に個別に作成することが推奨されています。
何に使われているトークンか後から思い出しやすくするため、
トークン名は`用途-機器名-作成日`のような規則で命名するとよいです。

:::

### ウェブ認証したい

```console
$ glab auth login --hostname gitlab.com
- Signing into gitlab.com
? How would you like to sign in?  # [Web | Token]
  // Webを選択 -> ブラウザで承認
? What domains ...(省略)...? # [gitlab.com,gitlab.com:443,registry.gitlab.com]
  // そのまま空欄でEnter
? Choose default protocol: # [SSH | HTTPS | HTTP]
  // SSHを選択

✓ Configured Git protocol.
✓ Configured API protocol.
✓ Logged in as <username>
✓ Configuration saved to /Users/<username>/.config/glab-cli
```

ウェブ認証を設定したときのログです。
`--hostname gitlab.com`で、GitLabホストを`gitlab.com`に指定して、`login`コマンドを実行しました。
プロンプトが表示されたので、そのまま対話的に選択して進めました。

認証方法で`Web`を選択しました。
ブラウザが起動したので、画面にしたがって承認しました。
ドメイン選択では、そのままEnterを押しました。
デフォルト値（`[giblab.com,gitlab.com:443,registory.gitlab.com]`）が設定されました。
Gitプロトコルは`SSH`を選択しました。
設定した内容が`~/.config/glab-cli/config.yml`に保存されました。

:::{note}

GitLabプロトコルは`SSH`もしくは`HTTPS`から選択します。
`HTTP`は選択してはいけません。

また、`SSH`を選択する場合、あらかじめGitLabにSSH鍵を登録しておく必要があります。
ちょっと使いたい場合は`HTTPS`でも構いません。

:::

### トークン認証したい

```console
$ glab auth login --hostname gitlab.com
- Signing into gitlab.com
? How would you like to sign in? [Web | Token]
  // Tokenを選択 -> PATを入力する流れになるはず
```

（あとで実行した結果を載せる）
（トークンはほぼ同時にGitLab上で作成して待機しておくとよさそう）


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

## ワークフロー

```console
# 新issueを起票（「なぜやるのか」→「なにをやるのか」を明確にする）
$ glab issue create \
  --title "Add feature" \
  --description "## 概要 ...\n\n## 具体的 ..." \
  --label "Type::Feature" \
  --label "Priority::High"

# 既存のissueを確認
$ glab issue list --assignee <username>
$ glab issue view <id>

# worktreeを作成
$ git fetch origin
$ git worktree add -B <branch-name> worktrees/<branch-name> origin/main
$ cd worktrees/<branch-name>
(worktrees/branch-name)$ git push -u origin <branch-name>

# コーディング
# Make changes
(worktrees/branch-name)$ git add --all
(worktrees/branch-name)$ git commit -m "feat: summary (refs #<id>)"
(worktrees/branch-name)$ git push

# パイプラインの確認
(worktrees/branch-name)$ glab ci status
(worktrees/branch-name)$ glab pipeline list

# マージリクエスト（下書き）を作成
# パイプラインが成功したら、MRの下書きを作成
(worktrees/branch-name)$ glab mr create \
  --source-branch <branch-name> \
  --target-branch main \
  --title "feat: title"
  --fill \
  --draft \
  --assignee @me
(worktrees/branch-name)$ glab mr view --web

# レビュー対応
# Fix feedbacks
(worktrees/branch-name)$ git add -A
(worktrees/branch-name)$ git commit -m "fix: address review comments (refs #id)"
(worktrees/branch-name)$ git push

# マージリクエストを更新
$ glab mr update <id> \
  --description "## 概要...\n\n## 変更点 ...\n\nCloses #<id>"
  --ready
$ glab mr view <id>

# マージ
$ glab mr merge --delete-source-branch

# 片付け
$ git worktree remove worktrees/<branch-name>
$ git fetch --prune
$ git worktrees prune
$ git branch -d <branch-name>
```
