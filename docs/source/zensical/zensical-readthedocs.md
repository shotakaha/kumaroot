# Read The Docs したい

```yml
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

Read the Docsで`zensical`を使えます。

```toml
# zensical.toml
[project]
site_url = "https://PROJECT_NAME.readthedocs.io/"
```

`zensical.toml`の設定で、canonical URLを明記する必要があるようです。

## リファレンス

- [Adding documentation project](https://docs.readthedocs.com/platform/stable/intro/add-project.html)
- [Deploying Zensical on Reat the Docs](https://docs.readthedocs.com/platform/stable/intro/zensical.html)
