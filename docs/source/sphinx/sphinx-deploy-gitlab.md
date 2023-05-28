# GitLab CIしたい（``.gitlab-ci.yml``）

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
