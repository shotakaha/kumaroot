# 自動化したい（``git-hooks``）

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

Gitには``hooks``と呼ばれる、自動化オプションが用意されています。
利用できるhooksのサンプルは{file}`プロジェクト/.git/hooks/`で確認できます。

ファイル名の末尾にある``.sample``を削除して有効にできます。
また、同名のファイルを作成してカスタマイズできます。

[pre-commit](../python/python-pre-commit.md)や[commitizen](../python/python-commitizen.md)など、これらのhooksファイルをカスタマイズするための外部ツールもあります。
