# ローカルの更新をリモートに反映（``git push``）

```console
$ git push
```

``push``コマンドを使って、ローカルに追加したコミットを、リモートに反映できます。

## すべてのタグをプッシュしたい

```console
$ git push origin --tags
```

リポジトリにあるタグをすべて、リモートリポジトリに反映させるには、プッシュ先に``origin``を指定し、``--tags``オプションをつけます。

## 既存のGitリポジトリを

```console
$ cd 既存のGitリポジトリ
$ git remote add origin リポジトリのURL
$ git branch -M main
$ git push -uf origin main
```

ローカルにすでにあるGitリポジトリも、GitHubやGitLabなどのホスティングサービスに追加できます。
``git remote add``を使って、プッシュ先のリポジトリのURLを指定します。
プッシュ先のリポジトリはあらかじめ作成しておきます。
