# リモートリポジトリしたい（``git remote``）

```console
$ git remote -v
origin  ssh://git@github.com/shotakaha/kumaroot.git (fetch)
origin  ssh://git@github.com/shotakaha/kumaroot.git (push)
```

`remote`コマンドで、リポジトリが紐づいている
リモートリポジトリの情報を確認できます。

## リモートリポジトリを確認したい（`show`）

```console
// git remote show リポジトリ名
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

## 複数のリモートリポジトリしたい

```console
// git remote add リポジトリ名 リモートリポジトリのURL
$ git remote add backup https://example.com/backup-repo.git

$ git remote -v
origin  ssh://git@github.com/shotakaha/kumaroot.git (fetch)
origin  ssh://git@github.com/shotakaha/kumaroot.git (push)
backup ...backup-repo.git (fetch)
backup ...backup-repo.git (push)
```

ひとつのリポジトリに、複数のリモートリポジトリを設定できます。
メインのリポジトリをGitHub、
そのバックアップをGitLab、という運用もできます。

```console
// pushする
// git push リポジトリ名 ブランチ名
$ git push origin main
$ git push backup main

// pullする
// git pull リポジトリ名 ブランチ名
$ git pull origin main
$ git pull backup main
```

`push`や`pull`するときに、リポジトリ名を指定できます。
デフォルトは`origin`です。

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

リポジトリのGit設定（`.git/config`）に`all`の設定を追加すると一括でプッシュできます。
