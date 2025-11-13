# パッケージ公開したい（`tyler`）

```console
$ tyler check
$ tyler build
```

`tyler`はTypstを公開する手順を（途中まで）自動化してくれるパッケージです。
`tyler.toml`で設定を変更できます。

## インストールしたい（`@mkpoli/tyler`）

```console
$ npm install -g @mkpoli/tyler
```

`tyler`はJavaScript/TypeScriptで作成されたCLIツールです。
`npm`を使ってシステムにインストールできます。

## 設定したい（`tyler.toml`）

```toml
[tool.tyler]
srcdir = "src"
outdir = "dist"
ignore = [
    "tests/",
    "examples/",
    "*.tmp",
    ".DS_Store",
]

[tool.tyler.validation]
check_manifest = true
check_structure = true
check_entrypoint = true

[tool.tyler.publish]
create_tags = true
run_tests = false
generate_docs = false
```

`tyler.toml`の`[tool.tyler]`セクションで設定します。
`srcdir`、`outdir`、`ignore`はビルド環境に応じで設定してください。

## ビルド前の確認したい（`tyler check`）

```console
$ tyler check --srcdir src
[Tyler] Checking package in /PATH/TO/PACKAGE...
[Tyler] Loaded typst.toml for package PACKAGE:0.2.0
[Tyler] Package name is valid: PACKAGE
[Tyler] Found 2492 packages in the Typst preview package index
[Tyler] The version of the package PACKAGE:0.2.0 is not published on the index, but it is not 0.1.0
[Tyler] Source directory found in /PATH/TO/PACKAGE/src
[Tyler] typst.toml is missing required package.entrypoint
```

`tyler check`コマンドでビルド設定をチェックできます。
設定が不足している場合は赤字で表示されます。
上記サンプルでは`typst.toml`に`package.entrypoint`が設定されていないことを教えてくれました。

```console
[Tyler] Source directory found in /PATH/TO/PACKAGE/src
[Tyler] Entrypoint src/ENTRYPOINT.typ found in /PATH/TO/PACKAGE/src/ENTRYPOINT.typ
[Tyler] Package authors are valid: AUTHOR
[Tyler] Package license is valid: MIT
[Tyler] License file found in /PATH/TO/PACKAGE/LICENSE
```

修正して再度`tyler check`した結果です。
Entrypointが確認でき、その後のチェックも進めることができました。

## ビルドしたい（`tyler build`）

```console
$ tyler build --srcdir src --install
[Tyler] Checking package in /PATH/TO/PACKAGE...
[Tyler] Loaded typst.toml for package PACKAGE:0.2.0
[Tyler] Package name is valid: PACKAGE
[Tyler] Source directory found in /PATH/TO/PACKAGE/src
[Tyler] Building package in /PATH/TO/PACKAGE...
[Tyler] Loaded typst.toml for package PACKAGE:0.2.0
[Tyler] Building for a unpublished package PACKAGE...
✔ current version: 0.2.0        ->            as-is 0.2.0    // バージョン選択
[Tyler] Bumping version by skip to 0.2.0...
[Tyler] The version of the package is not changed: 0.2.0
[Tyler] Bumped version in typst.toml to typst.toml
[Tyler] Source directory found in /PATH/TO/PACKAGE/src
[Tyler] Output directory will be  /PATH/TO/PACKAGE/dist
[Tyler] Copied typst.toml to dist/typst.toml
[Tyler] Copied README.md to dist/README.md
[Tyler] LICENSE is required but not found in /PATH/TO/PACKAGE
[Tyler] Copied src/COMPONENT1.typ to dist/COMPONENT1.typ
[Tyler] Copied src/COMPONENT2.typ to dist/COMPONENT2.typ
[Tyler] Copied src/COMPONENT3.typ to dist/COMPONENT3.typ
[Tyler] Copied src/COMPONENT4.typ to dist/COMPONENT4.typ
[Tyler] Installed to ~/Library/Application Support/typst/packages/local/PACKAGE/0.2.0
```

`tyler build`でローカルビルドできます。
ビルド結果は設定ファイル（`tyler.toml`）の`outdir`で設定したパスに生成されます。
この実行サンプルでは`dist/`に生成されています。

:::{note}

`typst.toml`の`[packages.entrypoint]`は、
`dist/`内の構造に合わせたパスに設定する必要があります。

:::

## ローカルインストールしたい（`tyler build --install`）

```console
$ tyler build --install
...
[Tyler] Installed to ~/Library/Application Support/typst/packages/local/PACKAGE/VERSION/
```

`tyler build --install`でローカルにインストールできます。
ビルドされたパッケージは（macOSの場合）
`~/Library/Application Support/typst/packages/local/`にインストールされます。

このパスにあるパッケージは、
`@local/PACKAGE:VERSION`
でインポートできるようになります。
公開前の自作パッケージを、他のパッケージからも使いたい場合に活用できます。

## パッケージを公開したい（`tyler build --install --publish`）

```console
$ tyler build --srcdir src --install --publish
[Tyler] Checking package in /PATH/TO/PACKAGE...
...（--install と同じなので省略）...
[Tyler] Installed to ~/Library/Application Support/typst/packages/local/PACKAGE/0.2.0
...（ここからが --publish 開始）...
[Tyler] Made a temporary directory in /var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tyler-publish
...（typst/packages をクローン）...
[Tyler] Cloned https://github.com/typst/packages.git into /var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tyler-publish/packages
[Tyler] Copied files from /PATH/TO/PACKAGE/dist to /var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tyler-publish/packages/packages/preview/PACKAGE/0.2.0
[Tyler] Tree of the copied files:
...（コピーしたファイルの一覧）...
[Tyler] Ran git -C /var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tyler-publish/packages add packages/preview/PACKAGE/0.2.0
[main 266e3088] PACKAGE@0.2.0
...（クローンしたリポジトリにパッケージを追加）...
[Tyler] Ran git -C /var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tyler-publish/packages commit -m PACKAGE@0.2.0
gh version 2.79.0 (2025-09-08)
https://github.com/cli/cli/releases/tag/v2.79.0
[Tyler] To publish the package, run the following commands:
...（パッケージ公開のPRするコマンドのテンプレート）...
  $ cd /var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tyler-publish/packages
  $ gh repo set-default https://github.com/typst/packages.git
  $ gh pr create --title "PACKAGE:0.2.0" --body-file ".github/pull_request_template.md" --draft
  $ cd -
Then go to your draft pull request on GitHub (following the link similar to https://github.com/typst/packages/pull/<number> from the output of the command above) and fill in the details to wait for the package to be approved
```

`--publish`オプションで、Typst Universeに公開する（一歩手前）の作業を自動化できます。
`tyler`が表示するログを順番に確認すればわかるとおり、
`/var/folders/`に、`typst/packages`の作業用Gitディレクトリを作成し、
`PACKAGE/dist/`に生成したビルド結果をコピーしてコミットしています。

実際にTypst Universeで公開するには、末尾にある`gh pr create`を実施し、
GitHubにPR（Pull Request）のドラフトを作成し、
承認を得るために必要なパッケージ概要を補足する必要があります。

## リファレンス

- [tyler - GitHub](https://github.com/mkpoli/tyler)
- [Typstのパッケージ作成補助ツールTylerを作った件 - Zenn](https://zenn.dev/mkpoli/articles/99c52202a1d1a8)
