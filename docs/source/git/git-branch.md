# ブランチしたい（`git branch`）

```console
$ git branch
  fix-git-branch
* main

$ git branch -a
  fix-git-branch
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/fix-git-branch
  remotes/origin/main
```

`git branch`で、ローカルのブランチを操作できます。
引数なしで実行すると、現在のブランチを一覧できます。
`*`がついているのが、現在の作業ブランチです。
`-a`オプションで、リモート（`/remotes/origin/`）も含めたすべてのブランチを確認できます。

## エイリアスしたい（`git br`）

```console
$ git config --global alias.br branch
```

`git branch`はよく使うGitコマンドのひとつなので、
エイリアスを作成しておくとよいです。

[Git本](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-Git-%E3%82%A8%E3%82%A4%E3%83%AA%E3%82%A2%E3%82%B9)にあるように、一般的に`br`がエイリアスとして使われます。

## ブランチを作成したい

```console
$ git branch ブランチ名
```

現在のブランチから、新しくブランチを作成できます。
ベースにするブランチ名が正しいか、必ず確認しましょう。
すでに存在する名前のブランチ名を指定すると、メッセージが表示されて失敗します。

## ブランチを削除したい（`git branch -d`）

```console
$ git branch -d ブランチ名
$ git branch -D ブランチ名  # 強制削除
```

`-d`オプションでブランチを削除できます。
指定したブランチの作業がまだマージされてない場合は、メッセージが表示されて失敗します。
`-D`オプションで強制削除できます。

## マージされたか確認したい

```console
// マージ済みのブランチを表示
$ git branch --merged

// マージされてないブランチを表示
$ git branch --no-merged
```

`--merged`オプションで、ブランチがマージ済みかどうか確認できます。
ローカルブランチの数を整理したい場合に使います。

## よく使うブランチ名

| semver | ブランチ名 | 用途 | 例 |
|---|---|---|---|
| `MAJOR` | `release` | リリース準備 | |
| `MINOR` | `feature` | 新機能の追加 | `feature-add-config` |
| `PATCH` | `fix` | バグ修正 | `fix-daq` |
| `PATCH` | `perf` | パフォーマンス改善 | `perf-daq` |
| - | `chore` | その他 | `chore-typo` |
| - | `docs` | ドキュメントの更新 | `docs-setup-packages` |
| - | `test` | ユニットテスト | `test-run_daq` |
| - | `style` | フォーマット | `style-format-ruff` |
| - | `ci` | CI/CDの修正 | `ci-gitlab-sphinx` |
| - | `build` | ビルド周りの修正 | `build-update-packages` |

ブランチ名にはprefixをつけることで、変更の意図を明確にできます。
上記は[semver](./git-semver.md)と合わせて使うことが多いブランチ名のサンプルです。
