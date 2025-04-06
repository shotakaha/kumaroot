# 作業ディレクトリしたい（`git worktree add`）

```console
// 作業ディレクトリの作成
$ cd プロジェクト名
$ git worktree add ../ディレクトリ名 ブランチ名
$ git worktree list

// 作業ディレクトリに移動
$ cd ../ディレクトリ名

// ソースコードの修正
$ git add 編集したファイル名
$ git commit  # コミットメッセージを編集
$ git push origin ブランチ名

// 作業ディレクトリの削除
$ cd ../プロジェクト名
$ git worktree remove ../ディレクトリ名
$ git worktree list

// ブランチを削除
$ git branch -d ブランチ名
$ git push origin --delete ブランチ名
```

`git worktree`で、任意のブランチを別ディレクトリで開発できます。

## 作業ディレクトリを作成したい（`git worktree add`）

```console
$ git worktree add ../ディレクトリ名 ブランチ名（or リモートブランチ名）
```

`git worktree add`で作業ディレクトリを作成できます。
作業ディレクトリは、プロジェクトの外側に作るのがよいそうです。

```console
$ git worktree ../worktrees/fix-番号 ブランチ名
```

僕はプロジェクトと同じ階層に`worktrees`というディレクトリを作成し、
その中にブランチ名に関連した作業ディレクトリを作成するようにしています。

## 作業ディレクトリを確認したい（`git worktree list`）

```console
[main] $ git worktree list
~/repos/プロジェクト名          8a6fd26 [main]
~/repos/worktrees/fix-75  8a6fd26 [75-fix-ブランチ名]
```

`git worktree list`で作業中のディレクトリを確認できます。
メインブランチ、開発ブランチのどちらからでも、同じ内容を確認できます。

## 作業ディレクトリを削除したい（`git worktree remove`）

```console
$ git worktree remove ../ディレクトリ名
```

`git worktree remove`で作業ディレクトリを削除できます。

:::{warning}

`rm -rf ../ディレクトリ名`で直接削除するのはNGです。
worktreeの情報は`.git/worktrees/`で管理されるため、
`rm`コマンドで直接削除すると、リポジトリの整合性が壊れる可能性があるそうです。

:::
