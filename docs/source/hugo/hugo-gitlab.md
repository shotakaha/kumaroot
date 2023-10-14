# GitLab CIしたい（``.gitlab-ci.yml``）

```yaml
image: registry.gitlab.com/pages/hugo/hugo_extended:latest

# Set this if you intend to use Git submodules
variables:
  GIT_SUBMODULE_STRATEGY: recursive
  HUGO_ENV: production

default:
  before_script:
    - git submodule update --init --recursive

test:
  script:
    - hugo
  rules:
    - if: $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH

pages:
  script:
    - hugo
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

## npmしたい

[Docsy](https://www.docsy.dev/)テーマのサイトで使っているCIです。

```yaml
image: node:18-buster-slim

variables:
  GIT_SUBMODULE_STRATEGY: recursive

before_script:
  # - apt-get update && apt-get install -y git --no-install-recommends
  - git submodule update --init --recursive
  - npm install

cache:
  paths:
    - node_modules/
    - public/

test:
  script:
    - node --version
    - npm --version
    - npm run build
  rules:
    - if: $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH

pages:
  script:
    - npm run build
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

ベースイメージはNodeにします。
``npm run コマンド名``はすべて``pakcage.json``で設定してあります。

```json
"scripts": {
    "prepare": "cd themes/docsy && npm install",
    "test": "echo \"Error: no test specified\" && exit 1",
    "develop": "hugo server",
    "build": "hugo",
}
```
