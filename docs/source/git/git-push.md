# ローカルの更新をリモートに送りたい（`git push`）

```console
$ git push [オプション] [リモート名 [ブランチ名]]
```

`git push`コマンドでローカルの変更（コミット）をリモートに反映できます。
現在のブランチに送り先（`upstream`）が設定されていない場合は、`--set-upstream`を指定するよう促すメッセージが表示されて失敗します。

:::{note}

`origin`は、リモートリポジトリにつけられた名前です。
`git clone`でリポジトリを取得したときに、取得元のURLに自動でつけられます。
名前は変更できますが、慣習的に`origin`が使われます。
リモートの一覧は`git remote -v`で確認できます（詳しくは`git-remote.md`を参照）。

:::

## 新規ブランチしたい

```console
$ git push origin 作業ブランチ名
 * [new branch]      作業ブランチ名 -> 作業ブランチ名
```

ローカルで作成したブランチを、リモート（`origin`）に新しく作成できます。
初めてプッシュするときは、次の`--set-upstream`も合わせて指定すると便利です。

## ブランチを紐づけたい（`--set-upstream`）

```console
$ git push -u origin 作業ブランチ名

$ git branch -a
* 作業ブランチ名
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/作業ブランチ名
  remotes/origin/main
```

`-u`（`--set-upstream`）オプションを付けると、ローカルのブランチとリモート（`origin`）のブランチを紐づけられます。
紐づけたあとは、`git push`だけでプッシュできます。

## タグしたい（`--tags`）

```console
$ git push origin --tags
```

`--tags`オプションを使って、ローカルで作成したすべてのタグを、リモート（`origin`）に追加できます。

## ブランチを削除したい（`--delete`）

```console
$ git push origin --delete 作業ブランチ名
```

`--delete`オプションを使って、リモート（`origin`）のブランチを削除できます。
ローカルのブランチは残ります。ローカルも削除したいときは`git branch -d`を使います。

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

これで、作成をはじめてしまったプロジェクトでもGitHub/GitLabで管理できるようになりました。
卒論や修論をLaTeXで書いている場合、ソースファイルをこのように管理しておいてもよいと思います
（執筆中はプライベートリポジトリを活用しましょう）。

:::{note}

2020年にGitHubで新規作成されるリポジトリのデフォルトブランチ名が`master`から`main`に変更されました。
2021年にはGitLabで新規作成されるプロジェクトのデフォルトブランチ名が`master`から`main`に変更されました。

:::
