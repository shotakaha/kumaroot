# 確認したい（`git status`）

```console
$ git status
```

`git status`でリポジトリの状態を確認できます。
おそらく、もっとも頻繁に使うコマンドです。

このコマンドを実行すると、

- 作業中のブランチ名（``On branch ブランチ名``）
- ステージされて**いる**ファイルの一覧（``Changes to be committed:``）
- ステージされて**いない**ファイルの一覧（``Changes not staged for commit:``）
- Git管理されていないファイルの一覧（``Untracked files:``）

などの状態を確認できます。

また、各ファイルに対する次の操作コマンドを教えてくれるので、
だいたいのことはマニュアルを読むことなく操作できます。

![](fig/git-status.png)
