# プッシュしたい（`git push`）

```console
$ git push [オプション] [リモート名 [ブランチ名]]
$ git push              # 現在のブランチを紐づけられたリモートにプッシュ
$ git push origin       # 現在のブランチをoriginにプッシュ
$ git push origin --tags  # タグをすべてoriginにプッシュ

// ブランチを指定してプッシュする場合
$ git push origin main  # mainブランチをoriginにプッシュ
$ git push origin feature-branch  # feature-branchをoriginにプッシュ
```

`git push`コマンドで、ローカルの変更（コミット）をリモートに反映（プッシュ）できます。
リモートリポジトリの名前は慣習的に`origin`が使われます。
現在のブランチに送り先（`upstream`）が設定されていない場合は、`--set-upstream`を指定するよう促すメッセージが表示されて失敗します。

## ブランチをプッシュしたい（`--set-upstream`）

```console
$ git push origin 作業ブランチ名
 * [new branch]      作業ブランチ名 -> 作業ブランチ名
```

`git push origin 作業ブランチ名`で、ローカルの作業ブランチをリモート（`origin`）に追加できます。
`[作業ブランチ名]`を省略すると、現在のブランチがプッシュされます。

```console
$ git push -u origin 作業ブランチ名
 * [new branch]      作業ブランチ名 -> 作業ブランチ名
$ git push --set-upstream origin 作業ブランチ名
 * [new branch]      作業ブランチ名 -> 作業ブランチ名

$ git branch -a
* 作業ブランチ名
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/作業ブランチ名
  remotes/origin/main
```

`-u / --set-upstream`オプションを付けると、ローカルの作業ブランチとリモート（`origin`）のブランチを紐づけられます。
ローカルで作成したブランチをはじめてリモートにプッシュするときに必要です。
一旦紐付けると、次回以降は`git push`だけでプッシュできます。


## タグをプッシュしたい（`--tags`）

```console
$ git push origin --tags
```

`--tags`オプションを使って、ローカルで作成したすべてのタグを、リモート（`origin`）に追加できます。

## ブランチを削除したい（`--delete`）

```console
$ git push origin --delete 作業ブランチ名
```

`--delete`オプションを使って、リモート（`origin`）のブランチを削除できます。
ローカルのブランチは残ります。
ローカルも削除したいときは`git branch -d`を使います。

## 既存のGitリポジトリを追加したい

```console
$ cd 既存のGitリポジトリ
$ git remote add origin リポジトリのURL
$ git branch -M main  # ブランチ名を main に変更
$ git push -u origin main
```

ローカルで作成したリポジトリを、GitHubやGitLabなどのホスティングサービスに追加できます。

まず、ホスティングサービス上に空のプロジェクトを作成します。
そして、`git remote add`を使って、ローカルのリポジトリと、ホスティングサービスのプロジェクトを紐づけます。
デフォルトのブランチ名は`main`に変更しておくとよいでしょう。
最後に、現在の作業ブランチ（`main`）をリモート（`origin`）にプッシュすればOKです。

これで、ローカルで作成をはじめてしまったプロジェクトでもGitHub/GitLabで管理できるようになりました。
卒論や修論をLaTeXで書いている場合、ソースファイルをこのように管理しておいてもよいと思います
（執筆中はプライベートリポジトリを活用しましょう）。

:::{note}

2020年にGitHubで新規作成されるリポジトリのデフォルトブランチ名が`master`から`main`に変更されました。
2021年にはGitLabで新規作成されるプロジェクトのデフォルトブランチ名が`master`から`main`に変更されました。

:::
