# リモートリポジトリしたい（`git remote`）

```console
$ git remote -v
origin  ssh://git@github.com/shotakaha/kumaroot.git (fetch)
origin  ssh://git@github.com/shotakaha/kumaroot.git (push)
```

`git remote`コマンドで、リポジトリが紐づいているリモートリポジトリを確認・管理できます。
まずは`-v`（`--verbose`）オプションでリモートの名前とURLを一覧できます。

## リモートリポジトリの詳細を確認したい（`show`）

```console
// git remote show リモートリポジトリ名
$ git remote show origin
* remote origin
  Fetch URL: ssh://git@github.com/shotakaha/kumaroot.git
  Push  URL: ssh://git@github.com/shotakaha/kumaroot.git
  HEAD branch: main
  Remote branch:
    main tracked
  Local branch configured for 'git pull':
    main merges with remote main
  Local ref configured for 'git push':
    main pushes to main (up to date)
```

`show`コマンドで、リモートリポジトリの詳細を確認できます。
どのブランチが紐づいているか、`git pull`や`git push`の対象かを確認できます。

## リモートリポジトリを追加したい（`add`）

```console
// git remote add リモートリポジトリ名 リモートリポジトリのURL
$ git remote add backup https://example.com/backup-repo.git

$ git remote -v
origin  ssh://git@github.com/shotakaha/kumaroot.git (fetch)
origin  ssh://git@github.com/shotakaha/kumaroot.git (push)
backup  https://example.com/backup-repo.git (fetch)
backup  https://example.com/backup-repo.git (push)
```

ひとつのリポジトリに、複数のリモートリポジトリを設定できます。
メインのリポジトリをGitHub、そのバックアップを別のホスティングサービス（例: GitLab）に置く、という運用もできます。

```console
// pushする
// git push リモートリポジトリ名 ブランチ名
$ git push origin main
$ git push backup main

// pullする
// git pull リモートリポジトリ名 ブランチ名
$ git pull origin main
$ git pull backup main
```

`push`や`pull`するときに、リモートリポジトリ名を指定できます。
省略すると、現在のブランチに紐づいたリモート（通常は`origin`）が使われます。

:::{seealso}

- [](./git-push.md)
- [](./git-pull.md)

:::

## 複数のURLに一括でプッシュしたい（`all`）

```conf
# .git/config
# リポジトリごとのGit設定
[remote "origin"]
    url = ssh://git@github.com/shotakaha/kumaroot.git
    fetch = +refs/heads/*:refs/remotes/origin/*

# all を追加
[remote "all"]
    url = https://example.com/origin-repo.git
    url = https://example.com/backup-repo.git
```

```console
$ git push all main
```

リポジトリのGit設定（`.git/config`）に`all`の設定を追加すると、`git push all`で複数のURLに一括でプッシュできます。

`git remote add`では URL を複数登録できません。
次のように`git config --add`で、2つ目以降の URL を追加することもできます。

```console
$ git remote add all https://example.com/origin-repo.git
$ git config --add remote.all.url https://example.com/backup-repo.git
```

:::{warning}

`git pull all`と`git fetch all`は、最初に登録したURLからしか取得しません。
バックアップ側の更新は取得されないので、取得は個別のリモートで行ってください。

:::

## リモートリポジトリを削除したい（`remove`）

```console
$ git remote remove backup  # git remote rm backup でも可
$ git remote -v
origin  ssh://git@github.com/shotakaha/kumaroot.git (fetch)
origin  ssh://git@github.com/shotakaha/kumaroot.git (push)
```

`remove`で、リモートリポジトリの設定を削除できます。
リモートリポジトリ（GitHubなど）上のデータは削除されません。
