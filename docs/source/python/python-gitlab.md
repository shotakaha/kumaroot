# GitLabしたい（`python-gitlab`）

```python
import gitlab
import os

# PATトークンはソースにベタ書きしない
# .env などに保存して管理する
token = os.getenviron["GITLAB_PAT_TOKEN"]
gl = gitlab.Gitlab(private_token=token)

# 認証（オプション）
gl.auth()

# プロジェクト一覧
projects = gl.projects.list(iterator=True)
for project in projects:
    print(project)
```

`python-gitlab`で、GitLab APIを操作できます。

## インストールしたい

`python-gitlab`パッケージをインストールします。
[gitlab](../command/command-gitlab.md)というCLIもインストールされます。

- `pipx`でインストール

```console
pipx install python-gitlab[autocompletion]
  installed package python-gitlab 4.11.1
  These apps are now globally available
    - gitlab
done! ✨ 🌟 ✨
```

- `poetry`でインストール

```console
$ poetry add python-gitlab --group dev
```

- `uv tool`でインストール

```console
$ uv tool install python-gitlab[autocompletion]
Installed 1 executable: gitlab
```

## リファレンス

- [python-giblab](https://python-gitlab.readthedocs.io/en/stable/index.html)
