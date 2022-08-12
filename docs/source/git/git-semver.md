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
$ pip3 install commitizen
```

## 設定ファイルを作成する（``cz init``）

プロジェクトルートで初期化（``cz init``）して、設定ファイルを作成します。
ターミナルに表示されるダイアログにしたがって矢印キーを使って選択します。

Pythonパッケージを開発している場合は``pyproject.toml``を設定ファイルにするとよいです。
その他の場合は、自分の好みの形式を選択すればよいと思います。僕は``.cz.toml``を選択する場合が多いです。

```bash
$ cd リポジトリ
$ cz init
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

## 変更をコミットする（``cz``）

``git commit``の代わりに``cz``を使います。

```bash
$ git add ステージするファイル名
$ cz
```

## バージョンアップする（``cz bump``）

コミットの内容をもとにした``semver``でバージョン番号を更新すると同時に、
タグを作成してくれます。
{option}`-ch`をつけると{file}`CHANGELOG.md`も更新できます。

```bash
$ cz bump
$ cz bump -ch
```

```{note}
使い始めてみるとすぐに気が付くと思いますが、
バージョンアップが先か、CHANGELOGの整理が先か問題があります。
僕はバージョンアップをしてから、CHANGELOGを整理することにしています。
```
