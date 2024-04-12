# GitLab Pagesしたい（``.gitlab-ci.yml``）

```yml
# ベースイメージ
default:
  image: node:21

variables:
  BASE_URL: $CI_PAGES_URL
  MISE_TARBALL: mise-v2024.4.4-linux-x64.tar.gz
  MISE_WGET_URL: https://github.com/jdx/mise/releases/download/v2024.4.4/$MISE_TARBALL

# キャッシュするディレクトリ
cache:
  paths:
    - .venv/
    - work/

# miseをダウンロードする場所を work とした
# work がキャッシュされていても失敗しないように、mkdir -p している
# TODO: 毎回ダウンロードしているが、ファイルに変更がない場合はスキップしたい
before_script:
  - pwd
  - mkdir -p work; cd work
  - if ! [ -e $MISE_TARBALL ]; then wget $MISE_WGET_URL && tar zxvf $MISE_TARBALL; fi
  - ./mise/bin/mise ls
  - ./mise/bin/mise bin-paths
  #- ./mise/bin/mise use node@21
  #- ./mise/bin/mise use python@3.12
  - ./mise/bin/mise use rye
  - ./mise/bin/mise bin-paths
  - pwd
  - cd ..
  - pwd
  - /root/.local/share/mise/installs/rye/latest/bin/rye config --set behavior.use-uv=true
  - /root/.local/share/mise/installs/rye/latest/bin/rye sync

pages:
  script:
    - pwd
    - cd mystmd
    - pwd
    - /root/.local/share/mise/installs/rye/latest/bin/rye run myst build --html
    - mv _build/html/ ../public/
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

deploy:
  stage: deploy
  script: echo "Define your deployment script!"
  environment: production
```

[MyST](https://myst-tools.orge)でドキュメントをビルドするために、PythonとNodeが必要です。
いろいろ試した結果、ベースイメージは``node:21``にすることにしました。
あとは、必要なツールを逆算して、

1. mise: [リリースページ](https://github.com/jdx/mise/releases)からビルド済みバイナリーをダウンロード
2. Rye: [mise](https://mise.jdx.dev)でインストール
3. Python: [Rye](https://rye-up.com/)でインストール

することにしました。

:::{admonition} いろいろ試したこと

1. ``mise use python@3.12``すると、インストールに時間がかかるのでやめました
2. ``image: rust``にして``cargo install mise``も5分以上かかったのでやめました
3. ``image: python:3.12``で残りを整えても、``myst build --html``でNodeがなくて怒られました。``/root/.local/...``にNodeはインストールしてあるのですが、パスの通し方がわからないのでやめました。
4. ``image: node:21-slim``にしたら、イメージ準備にかかる時間は減りましたが、後ろの方でエラーがでたのでやめました

ということで。
結果、``node:21``をベースにして、そこにPython環境を構築することにしました。
:::

