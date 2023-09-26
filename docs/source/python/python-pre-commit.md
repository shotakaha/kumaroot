# コミットをチェックしたい（``pre-commit``）

```console
$ pip3 install pre-commit
```

コードをフォーマッタやリンターなどのチェック作業は、コミットする前に自動化できると便利です。
[pre-commit](https://pre-commit.com/)を使うと、Gitのpre-commit hooksを簡単に管理できます。

以下ではフォーマッタに[black](./python-black.md)、リンターに[ruff](./python-ruff.md)を使う方法で設定します。
