# GitLab CIしたい（``.gitlab-ci.yml``）

{file}`.gitlab-ci.yml`でGitLab CIを設定することで、Sphinxを使ったGitLab Pagesを自動でビルトできます。
以下は、
シンプルに``sphinxdoc/sphinx``イメージを使う方法と、
``python``イメージと``poetry``を使う方法のサンプルです。

コメントアウトしている部分があったり、デバッグ用の出力があったりしますが、
不要なものは適当にスキップして使ってください。

## Sphinxイメージを使いたい

```yaml
image: sphinxdoc/sphinx:latest
# image: sphinxdoc/sphinx-latexpdf:latest

# stages:
# - test

# sast:
#   stage: test
# include:
# - template: Security/SAST.gitlab-ci.yml

variables:
  PIP_CACHE_DIR: '$CI_PROJECT_DIR/.cache/pip'

cache:
  paths:
    - .cache/pip
    - venv/

before_script:
  - python -V
  - pip --version
  - pip install -r requirements.txt


test:
  script:
    - pip install black
    - black --check .
    # build HTML pages
    - cd docs; make dirhtml
    - ls -ltr _build/
    - ls -ltr _build/dirhtml/
  except:
    - master

pages:
  stage: deploy
  script:
    # build HTML pages
    - cd docs; make dirhtml
    - mv _build/dirhtml/ ../public/
    # build PDF
    # - make latexpdf
    # - mv _build/latex public/
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

[Sphinx公式のDockerイメージ](https://hub.docker.com/r/sphinxdoc/sphinx)を使うときの設定です。
依存関係は``pip install -r requirements.txt``で追加インストールしています。
PDFを生成したい場合はイメージを``sphinx-latexpdf``に変更してください。

## Poetryを使いたい

```yaml
# Official language image. Look for the different tagged releases at:
# https://hub.docker.com/r/library/python/tags/
image: python:latest

# Change pip's cache directory to be inside the project directory since we can
# only cache local items.
variables:
  PIP_CACHE_DIR: '$CI_PROJECT_DIR/.cache/pip'

# Pip's cache doesn't store the python packages
# https://pip.pypa.io/en/stable/reference/pip_install/#caching
#
# If you want to also cache the installed packages, you have to install
# them in a virtualenv and cache it as well.
cache:
  paths:
    - .cache/pip
    - venv/

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
  #- poetry config virtualenv.in-project true
  #- pip install -r requirements.txt

pages:
  script:
    - cd docs; make dirhtml
    - mv _build/dirhtml/ ../public/
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

``Poetry``で環境構築したい場合の設定です。
ベースは[Python公式のDockerイメージ](https://hub.docker.com/_/python)を使っています。
そこに``virtualenv``で仮想環境を作成した上で、さらに``Poetry``で環境を構築しています。

依存パッケージにGitHubリポジトリを指定している場合など、``pip install -r requirements.txt``では解決できない場合に有効な設定だと思います。
