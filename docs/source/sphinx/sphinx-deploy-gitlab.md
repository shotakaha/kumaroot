# GitLab CIしたい（``.gitlab-ci.yml``）

GitLab CIを設定することで、Sphinxで生成したドキュメントを
GitLab Pagesに自動で公開できるようになります。
設定は{file}`.gitlab-ci.yml`に記述します。

以下では、
``sphinxdoc/sphinx``イメージを使う方法と、
``python``イメージで``poetry``を使う方法のサンプルです。

コメントアウトしている部分があったり、デバッグ用の出力があったりしますが、
不要なものは適当にスキップして使ってください。

## Sphinxイメージを使いたい

```yaml
# 環境変数の設定
variables:
  PIP_CACHE_DIR: '$CI_PROJECT_DIR/.cache/pip'

# キャッシュするパスの設定
cache:
  paths:
    - .cache/pip
    - venv/

default:
  image: sphinxdoc/sphinx:latest
  # image: sphinxdoc/sphinx-latexpdf:latest
  before_script:
    - python -V
    - pip --version
    - pip install virtualenv
    - virtualenv venv
    - source venv/bin/activate
    - pip install -U pip
    - pip install -r requirements.txt

test:
  script:
    # build HTML pages
    - cd docs; make dirhtml
    - ls -ltr _build/
    - ls -ltr _build/dirhtml/
  rules:
    - if: $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH

pages:
  stage: deploy
  script:
    # build HTML pages
    - cd docs
    - make dirhtml
    - mv _build/dirhtml/ ../public/
    # - make latexpdf
    # - mv _build/latex/ファイル名.pdf ../public/
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

[Sphinx公式のDockerイメージ](https://hub.docker.com/r/sphinxdoc/sphinx)を使うときの設定です。
依存関係は``pip install -r requirements.txt``で追加インストールしています。
PDFを生成したい場合はイメージを``sphinx-latexpdf``に変更してください。

## Python + Poetryを使いたい

```yaml
# Change pip's cache directory to be inside the project directory since we can
# only cache local items.
variables:
  PIP_CACHE_DIR: '$CI_PROJECT_DIR/.cache/pip'

# キャッシュするパスを設定
# Pip's cache doesn't store the python packages
# https://pip.pypa.io/en/stable/reference/pip_install/#caching
cache:
  paths:
    - .cache/pip
    - venv/

default:
  # 利用するイメージを設定
  # Pythonのバージョンは以下で確認
  # https://hub.docker.com/r/library/python/tags/
  image: python:3.12
  # ジョブの前に実行するスクリプトを設定
  # virtualenvで仮想環境を作成し、そこのpoetryを追加
  # poetry install で関係するパッケージを追加
  # APIドキュメントのときは poetry install する
  # ただのドキュメントの poetry install --no-root でもOK
  before_script:
    - python -V # Print out python version for debugging
    - pip install virtualenv
    - virtualenv venv
    - source venv/bin/activate
    - pip install -U pip
    - pip install -U poetry
    - which poetry
    - poetry env info --path
    - poetry install
    # もしくは
    # - poetry install --no-root

# デフォルトブランチ以外にプッシュがあった場合：
# ページがビルドできるかだけ確認する
# （ページを公開しない）
test:
  script:
    - poetry show --outdated
    - cd docs; make dirhtml; cd ..;
    - ls -ltr docs/_build/dirhtml/
  rules:
    - if: $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH

# デフォルトブランチにプッシュ（やマージリクエスト）があった場合：
# ページをビルドし、GitLab Pagesに公開する
# "public"というartifactで公開している
pages:
  stage: deploy
  script:
    - cd docs; make dirhtml; cd..;
    - mv docs/_build/dirhtml/ public/
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

``Python + Poetry``で環境構築する場合の設定です。
ベースとなるイメージは[Python公式のDockerイメージ](https://hub.docker.com/_/python)を使っています。

root権限でpipすると警告が表示されるため、
``virtualenv``で仮想環境を作成した上に
``Poetry``で環境を構築しています。

## リファレンス

- [sphinxdoc/sphinx - DockerHub](https://hub.docker.com/r/sphinxdoc/sphinx)
- [python/python - DockerHub](https://hub.docker.com/_/python)
