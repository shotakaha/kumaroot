# GitLab CIしたい

```yaml
stages:
  - build
  - test
  - deploy

variables:
  変数名1: 値1
  変数名2: 値2

default:
  image: デフォルトのイメージ名
  cache:
    - キャッシュのパス
  before_script
    - すべてのジョブに共通する実行内容

ジョブ名:
  stage: ステージ名
  image: イメージ名
  script:
    - このジョブのメインの実行内容

```

クリエーションライン株式会社が[GitLabの日本語マニュアル](https://gitlab-docs.creationline.com/)を作成し、公開してくれています。
とりあえず使い方に困ったら、このサイトを参照するとよいです。

## キーワードをしりたい

GitLab CI/CDには、パイプラインに対して設定するグローバルキーワードと、
ジョブに対して設定するジョブキーワードがあります。
詳細は[GitLab CIのキーワードリファレンス](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html)を参照してください。

## デフォルト設定したい（``default``）

```yaml
default:
  image: python:3.11
  before_script:
    - pip install -U pip
    - pip install -U virtualenv
    - virtualenv venv
    - source venv/bin/activate
```

[default](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html#default)キーワードで、パイプラインのデフォルト動作を定義できます。
その中身は、ジョブキーワードが利用できます。
上のサンプルは、Pythonを使ったプロジェクトで、僕がよく使っている設定です。
すべてのジョブで実行する内容を[before_script](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html#before_script)に書いています。

:::{note}

パイプラインでPythonを使う場合は、まず仮想環境を作成することが推奨されています。
そのまま``pip``を使うと以下の警告が出力されます。

```console
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager.
It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```

:::

:::{note}

``before_script``をトップレベルに定義するのは、現在は推奨されていません。
``default``の中に書くか、ジョブの中に書く必要があります。

:::

## 環境変数したい（``variables``）

```yaml
variables:
  BASE_URL: "$CI_PAGES_URL"
  PIP_CACHE_DIR: '$CI_PROJECT_DIR/.cache/pip'
```

[variables](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html#variables)キーワードで、パイプラインで使う環境変数（CI/CD変数）を定義できます。
このキーワードは、グローバルに対しても、ジョブに対しても利用できます。
グローバルキーワードとして定義した場合は、すべてのジョブのデフォルト設定として利用できます。
ジョブキーワードとして同じ変数名を定義した場合は、ジョブの設定値が優先されます。

## キャッシュしたい（``cache``）

```yaml
default:
  image: python:3.11
  cache:
    key: キーワード
    paths:
      - .cache/pip
      - venv
```

[cache](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html#cache)キーワードで、ジョブ間で共有するキャッシュのパスを定義できます。
`paths`フィールドで、パスを設定します。
`key`フィールドで、キャッシュのIDを設定できます。

## 実行条件したい（``rules``）

```yaml
test:
  script:
    - テストを実行
  rules:
    - if: $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH
```

[rules](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html#rules)キーワードで、ジョブを実行する条件を定義できます。
上のサンプルでは、条件が**コミットされたブランチ名がデフォルトブランチ名と一致しない**場合にテストが走るように設定しています。
つまり、作業ブランチにコミットしたときに、テストが走るようになっています。

:::{note}

``rules``の代わりに``only/except``を使うことは推奨されていないみたいです。
過去のブログ記事などを参考にしてパイプラインを作成した場合は、移行するとよいです。

:::

## ファイルを保存したい（``artifacts``）

```yaml
pages:
  script:
    - make dirhtml
    - mv _build/html/ public/
  artifacts:
    paths:
      - public
    expire_in: "30 days"
```

[artifacts](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html#artifacts)キーワードで、保存するファイルを定義できます。
上のサンプルはGitLab PagesにSphinxで生成したドキュメントを公開するための設定です。
[expire_in](https://gitlab-docs.creationline.com/ee/ci/yaml/index.html#artifactsexpire_in)を使って、アーティファクトの保存期限を設定できます。
GitLabの無料ユーザーの場合、リポジトリの上限が10GiBとなっています。
必要のないアーティファクトは期限をつけて定期的に削除設定することをオススメします。
