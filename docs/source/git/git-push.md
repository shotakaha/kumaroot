# ローカルの更新をリモートに反映（``git push``）

```console
$ git push
```

``push``コマンドを使って、ローカルの作業ブランチに追加したコミットを、リモートに反映できます。
ブランチ名が一致しない場合は、メッセージが表示されて失敗します。

## 新規ブランチしたい

```console
$ git push origin 作業ブランチ名
 * [new branch]      作業ブランチ名 -> 作業ブランチ名

$ git br -a
* 作業ブランチ
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/作業ブランチ名
  remotes/origin/main
```

ローカルで作成した作業ブランチからプッシュする場合、
リモート先（``origin``）と、そのブランチを紐づける必要があります。

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
