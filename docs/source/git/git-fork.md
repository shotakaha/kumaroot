# フォーク開発したい

```console
$ gh repo fork OWNER/REPO
```

「フォーク」とは第三者のリポジトリを自分のアカウントにコピーする作業です。
これにより、自分のリポジトリを作業スペースとして、元の開発に安全に協力できます。

GitHub上のリポジトリは`gh`コマンドでフォーク＆クローンを作成できます。

:::{note}

GitLabにもフォーク機能はありますが、
フォークを活用した共同開発は、
どちらかといえばGitHubに根付いている文化のようです。

:::

## 手動でフォークしたい

```console
// GitHub上で「自分がフォークした」リポジトリ
$ git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
$ cd REPOSITORY_NAME

// 「元のリポジトリ」をupstreamとして登録
$ git remote add upstream https://github.com/ORIGINAL_OWNER/REPOSITORY_NAME.git

$ git remote --verbose
origin    https://github.com/YOUR_USERNAME/project.git (fetch)
origin    https://github.com/YOUR_USERNAME/project.git (push)
upstream  https://github.com/ORIGINAL_OWNER/project.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/project.git (push)

// 事故防止：upstreamにpush禁止
$ git remote set-url --push upstream DISABLED

// 設定を確認
$ git remote --verbose
origin    https://github.com/YOUR_USERNAME/project.git (fetch)
origin    https://github.com/YOUR_USERNAME/project.git (push)
upstream  https://github.com/ORIGINAL_OWNER/project.git (fetch)
upstream  DISABLED
```

ブラウザなどでフォークしたリポジトリを、手動でクローンしてセットアップする手順です。
`upstream`として設定したオリジナルのリポジトリに`git push`できないようにすることで、誤操作を防ぎ、安全に管理できるようにしています。

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
