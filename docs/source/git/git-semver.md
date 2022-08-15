# semverしたい

``semver``（semantic versioning）はバージョン番号を管理する手法のひとつです。
``Major.Minor.Patch``の3つの数字で表現し、それぞれ次の意味を持たせて利用します。

``Major``
: **後方互換性のない**機能を追加したり、変更を加えた場合に +1

``Minor``
: 後方互換性がある機能を追加した場合に +1

``Patch``
: 後方互換性があるバグ修正をした場合に +1

これを自分の頭で考えて管理するのは（僕にとっては）到底無理なので、
[commitizen](https://commitizen-tools.github.io/commitizen/)というツールを使っています。

```{note}
僕はPythonで書かれた``commitizen``を使っています。
JavaScriptで書かれたnpmパッケージの``commitizen``もありますが、別物のようです。
```

## インストール

グローバルにインストールするとよいと思います。

```bash
pip3 install commitizen
```

## 設定ファイルを作成する（``cz init``）

プロジェクトルートで初期化（{command}`cz init`）して、設定ファイルを作成します。
ターミナルに表示されるダイアログにしたがって矢印キーで選択します。

Pythonパッケージを開発している場合は{file}`pyproject.toml`を設定ファイルにするとよいです。
その他の場合は、自分の好みの形式を選択すればよいと思います。僕は{file}`.cz.toml`を選択する場合が多いです。

```bash
cd リポジトリ
cz init
```

生成された設定ファイルは次のようになっているはずです。
最近のPythonパッケージは（暗黙の）ルールとして
``[tool.パッケージ名]``の下に設定を書くようになっています。
（ただの慣習なのか、それを定義したPEPが存在するかは未確認です）

```toml
[tool]
[tool.commitizen]
name = "cz_conventional_commits"
version = "0.0.1"
tag_format = "$version"
```

### バージョン番号を一元管理する

バージョン番号を書くファイルに決まりはありません。
たとえば、``src/__init__.py``だったり``src/__version__.py``だったり、
ひと（やチーム）によってさまざまだと思います。
``[tool.commitizen.version_files]``を設定すると、
これらの外部ファイルにあるバージョン番号も
まとめて更新できるようになります。

```toml
[tool]
[tool.commitizen]
...
version_files = [
    "pyproject.toml:version"
    "src/__init__.py",
]
```

## 変更をコミットする（``cz c``）

{command}`git commit`の代わりに{command}`cz c`を使います。

```bash
git add ステージするファイル名
cz c
```

### コミットの種類を選択する

```bash
? Select the type of change you are committing (Use arrow keys)
 » fix: A bug fix. Correlates with PATCH in SemVer
   feat: A new feature. Correlates with MINOR in SemVer
   docs: Documentation only changes
   style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
   refactor: A code change that neither fixes a bug nor adds a feature
   perf: A code change that improves performance
   test: Adding missing or correcting existing tests
   build: Changes that affect the build system or external dependencies (example scopes: pip, docker, npm)
   ci: Changes to our CI configuration files and scripts (example scopes: GitLabCI)
```

### 変更のスコープを入力する

```bash
? What is the scope of this change? (class or file name): (press [enter] to skip)
```

### 変更内容を簡単に説明する

```bash
? Write a short and imperative summary of the code changes: (lower case and no period)
```

### 追加の説明があれば入力する

```bash
? Provide additional contextual information about the code changes: (press [enter] to skip)
```

### 後方互換性のあり／なし

```bash
? Is this a BREAKING CHANGE? Correlates with MAJOR in SemVer (y/N)
```

### 補足情報があれば入力する

```bash
? Footer. Information about Breaking Changes and reference issues that this commit closes: (press [enter] to skip)
```

### コミットメッセージの形式を確認

```bash
feat(git/git-semver.md): semverを追加した

[main 1ecb61d] feat(git/git-semver.md): semverを追加した
 2 files changed, 101 insertions(+)
 create mode 100644 docs/source/git/git-semver.md

Commit successful!
```

## バージョンアップする（``cz bump``）

コミットの内容をもとにした``semver``でバージョン番号を更新すると同時に、
タグを作成してくれます。
{command}`-ch`をつけると{file}`CHANGELOG.md`も更新できます。

```bash
cz bump
cz bump -ch
```

```{note}
使い始めてみるとすぐに気が付くと思いますが、
バージョンアップが先か、CHANGELOGの整理が先か問題があります。
僕はバージョンアップをしてから、CHANGELOGを整理することにしています。
```
