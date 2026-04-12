# Read The Docs したい

```yaml
# .readthedocs.yml
version: 2

build:
  on: ubuntu-24.04
  tools:
    python: latest
  jobs:
    install:
      - pip install zensical
    build:
      html:
        - zensical build
    post_build:
      - mkdir -p $READTHEDOCS_OUTPUT/html/
      - cp --recursive site/* $READTHEDOCS_OUTPUT/html/
```

Read the Docsでも`zensical`を使えるようです。
`.readthedocs.yml`の`build.jobs.build.html`に`zensical build`を指定するだけで、ビルドコマンドとして`zensical build`が実行されます。

```toml
# zensical.toml
[project]
site_url = "https://PROJECT_NAME.readthedocs.io/"
```

`zensical.toml`の設定で、canonical URLを明記する必要があるようです。

:::{note}

Read the Docsへの適用はまだですが、ローカル環境でビルドできることは確認しました。
`mkdocs.yml`はそのままで、
`mkdocs`から`zensical`に置き換えるだけでOKでした。
Read the Docsでのビルドが成功したら、追記します。
:::

## リファレンス

- [Adding documentation project](https://docs.readthedocs.com/platform/stable/intro/add-project.html)
- [Deploying Zensical on Read the Docs](https://docs.readthedocs.com/platform/stable/intro/zensical.html)
