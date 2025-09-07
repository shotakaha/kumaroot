# フォーク開発したい

```console
// GitHub上でフォークしたリポジトリ
$ git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
$ cd REPOSITORY_NAME

// 元のリポジトリをupstreamとして追加
$ git remote add upstream https://github.com/ORIGINAL_OWNER/REPOSITORY_NAME.git

$ git remote --verbose
origin    https://github.com/YOUR_USERNAME/project.git (fetch)
origin    https://github.com/YOUR_USERNAME/project.git (push)
upstream  https://github.com/ORIGINAL_OWNER/project.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/project.git (push)

// 事故防止
$ git remote set-url --push upstream DISABLED
$ git remote --verbose
origin    https://github.com/YOUR_USERNAME/project.git (fetch)
origin    https://github.com/YOUR_USERNAME/project.git (push)
upstream  https://github.com/ORIGINAL_OWNER/project.git (fetch)
upstream  DISABLED
```

:::{seealso}

- [](./git-remote.md)

:::

## 元のリポジトリの最新状態を取得したい

```console
$ git switch main
$ git fetch upstream
$ git merge upstream/main
$ git push origin
```

## 元のリポジトリへのプッシュを禁止したい

```console
$ git remote set-url --push upstream DISABLED

// 他に
$ git remote set-url --push upstream NO_PUSH
$ git remote set-url --push upstream READONLY
$ git remote set-url --push upstream FORBIDDEN
$ git remote set-url --push upstream DENIED
```

元のリポジトリ（`upstream`）に間違えてプッシュしないための設定です。
プッシュ用のURLを無効なURLを設定します。
任意の文字列で構いませんが、
`DISABLED`、
`NO_PUSH`、
`READONLY`
などがよく使われるようです。

## ブランチを作成したい

```console
$ git switch main
$ git pull upstream main
$ git switch --create feature/<new-branch-name>

$ git add <edited-files>
$ git commit -m "feat: add new implementation"

$ git push --set-upstream origin feature/<new-branch-name>
```

## ブランチを整理したい

```console
$ git switch main
$ git branch --delete feature/<merged-feature>
$ git remote prune origin
```

## プルリクエストしたい

```console
// 新しいブランチを作成して切り替え
$ git switch --create feature/<new-branch-name>

// 自分のフォークにプッシュ
$ git push -u origin feature/<new-branch-name>

// GitHub上で「Compare & Pull Request」
```

開発ブランチを **自分のフォーク** にプッシュします。
リモートに開発ブランチがない場合は
`git push --set-upstream`します。
リモートブランチが存在する場合は
`git push`で大丈夫です。
