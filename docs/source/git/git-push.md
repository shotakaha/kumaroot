# ローカルの更新をリモートに送りたい（``git push``）

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

``--tags``オプションを使って、ローカルで作成したすべてのタグを、リモート（``origin``）に追加できます。

## 既存のGitリポジトリを追加したい

```console
$ cd 既存のGitリポジトリ
$ git remote add origin リポジトリのURL
$ git branch -M main  # ブランチ名を main に変更
$ git push -uf origin main
```

ローカルで作成したリポジトリを、GitHubやGitLabなどのホスティングサービスに追加できます。

まず、ホスティングサービス上に空のプロジェクトを作成します。
そして、``git remote add``を使って、ローカルのリポジトリと、ホスティングサービスのプロジェクトを紐づけます。
デフォルトのブランチ名は``main``に変更しておくとよいでしょう。
最後に、現在の作業ブランチ（``main``）をリモート（``origin``）にプッシュすればOKです。

これで、作成をはじめてしまったプロジェクトでもGitHub/GitLabで管理できるようになりました。
卒論や修論をLaTeXで書いている場合、ソースファイルをこのように管理しておいてもよいと思います
（執筆中はプライベートリポジトリを活用しましょう）。

:::{note}

2020年にGitHubのデフォルトリポジトリ名が``master``から``main``に変更されました。
2021年にはGitLabのデフォルトリポジトリ名が``master``から``main``に変更されました。

:::
