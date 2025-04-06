```{eval-rst}
.. index::
    pair: Git; usage
```

# Gitの使い方

Gitはバージョン管理ツールです。ひとりでも気軽にはじめることができます。
ソースコードに限らず、テキスト形式のファイルの管理が得意です。
とてもとても簡単に導入できるので、修論や博論を執筆中の方は、いますぐ使いはじめることをオススメします！！

## セットアップしたい

```{toctree}
---
maxdepth: 2
---
git-setup
```

## リポジトリ操作したい

```{toctree}
---
maxdepth: 2
---
git-status
git-add
git-commit
git-restore
git-log
git-tag
git-branch
git-switch
git-checkout
git-merge
git-diff
git-rm
git-revert
```

## リモートリポジトリしたい

```{toctree}
---
maxdepth: 1
---
git-remote
git-clone
git-fetch
git-pull
git-push
git-submodule
```

## CI/CDしたい

Gitホスティングサービスを使う利点のひとつとして、
継続的な開発サイクル（Continuous Integration / Continuous Delivery）の自動化があります。
GitLabは[GitLab CI](https://docs.gitlab.com/ee/ci/)、GitHubは[GitHub Actions](https://docs.github.com/ja/actions)という名前で利用できます。

```{toctree}
---
maxdepth: 1
---
git-gitlab-ci
git-github-actions
```

## もっとGitしたい

```{toctree}
---
maxdepth: 1
---
git-single
git-semver
git-flow
git-gitlab
git-hooks
git-lfs
git-cliff
git-review
```

## 関連ドキュメント

* [Git本家](https://git-scm.com)
* [サルでもわかるGit入門](https://backlog.com/ja/git-tutorial/)
* [gitflow](https://github.com/nvie/gitflow)
* [Vincent Driessen's Succesful Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
* [Git Flow Cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/index.ja_JP.html)
