# 自動化したい（``git-hooks``）

`Git Hooks`は、Gitコマンドに連動したジョブを実行できる仕組みです。
よく使われている（と思われる）フック名と、実行されるタイミング、
実行するとよいコマンドを整理してみました。

| フック名 | 説明 | コマンド |
|---|---|---|
| `pre-commit` | コミットメッセージを入力する前 | `ruff` |
| `prepare-commit-msg` | エディターが起動する前 | |
| `commit-msg` | コミットメッセージを保存した後 | `commitizen` |
| `post-commit` | コミットが完了した後 | |
| `pre-push` | プッシュする前 | `poetry`、`pytest` |

Hooksはシェルスクリプトで作成し`プロジェクト/.git/hooks/`に配置します。
ただし、[pre-commit](../python/python-pre-commit.md)や[commitizen](../python/python-commitizen.md)など、これらのhooksをカスタマイズするための外部ツールを使うとより簡単に設定を変更できます。

## サンプルを確認したい

```console
$ ls .git/hooks/
applypatch-msg.sample
commit-msg.sample
fsmonitor-watchman.sample
post-update.sample
pre-applypatch.sample
pre-commit.sample
pre-merge-commit.sample
pre-push.sample
pre-rebase.sample
pre-receive.sample
prepare-commit-msg.sample
push-to-checkout.sample
update.sample
```

Gitリポジトリを初期化すると
`プロジェクト/.git/hooks/`にサンプルが自動で生成されます。
ファイル名の末尾にある``.sample``を削除して有効にできます。
また、同名のファイルを作成してカスタマイズできます。

## リファレンス

- [Git Hooks - git-scm.com](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA-Git-%E3%83%95%E3%83%83%E3%82%AF)
