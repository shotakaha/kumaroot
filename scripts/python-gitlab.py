# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# # GitLab APIの確認

import os
import requests
import time

# テスト用のリポジトリを作成した
#
# - https://gitlab.com/jacst/api-test

PROJECT_ID = "62069387"
ENDPOINT = "https://gitlab.com/api/v4"
TOKEN = os.environ["GITLAB_TOKEN"]
# scope: api
# expires: 2024-10-27

# プロジェクト情報を取得
#
# - `GET`
# - `https://gitlab.com/api/v4/projects/{プロジェクトID}`

url = f"{ENDPOINT}projects/{PROJECT_ID}/"
url

# # ブランチAPI
#
# https://gitlab-docs.creationline.com/ee/api/branches.html

# ## ブランチを確認する
#
# エンドポイント
#
# ```
# GET /projects/:id/repository/branches/:branch
# ```
#
# リクエストの例
#
# ```console
# $ curl
# --header "PRIVATE-TOKEN: <your_access_token>"
# "https://gitlab.com/api/v4/projects/:id/repository/branches/:branch"
# ```
#
# 引数
#
# - `:id` = `project_id`
# - `:branch` = `branch_name`
#
# レスポンス
#
# ステータスコードを確認
#
# - ブランチがある: 200
# - ブランチがない: 404 `{'message': '404 Branch Not Found'}`

# +
# 必要な引数
project_id = PROJECT_ID
branch_name = "main"
branch_name = "test_branch"

# エンドポイント
url = f"{ENDPOINT}/projects/{project_id}/repository/branches/{branch_name}"

# ヘッダー
headers = {
    "PRIVATE-TOKEN": TOKEN,
}

try:
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
except Exception as e:
    print(e)

print(response.ok)
print(response.status_code)
response.json()
# -

# ## ブランチを作成する
#
# エンドポイント
#
# ```
# POST /projects/:id/repository/branches
# ```
#
# リクエストの例
#
# ```console
# $ curl
# --request POST
# --header "PRIVATE-TOKEN: <your_access_token>"
# "https://gitlab.com/api/v4/projects/:id/repository/branches?branch=newbranch&ref=main"
# ```
#
# 引数
#
# - `:id` = `project_id`
# - `:branch` = `new_branch`
# - `:ref` = `base_branch`
#
# レスポンス
#
# - 成功: 201
# - 失敗: 400 `{'message': 'Branch already exists'}`

# +
# 必要な引数
project_id = PROJECT_ID
new_branch = "test_branch8"
base_branch = "main"

# エンドポイント
url = f"{ENDPOINT}/projects/{project_id}/repository/branches"

# ヘッダー
headers = {
    "PRIVATE-TOKEN": TOKEN,
}

# クエリ
data = {
    "branch": new_branch,
    "ref": base_branch,
}

try:
    response = requests.post(url, headers=headers, data=data, timeout=10)
    response.raise_for_status()
except Exception as e:
    print(e)

print(response.ok)
print(response.status_code)
response.json()
# -

# ## ブランチを削除する
#
# エンドポイント
#
# ```
# DELETE /projects/:id/repository/branches/:branch
# ```
#
# リクエストの例
#
# ```console
# $ curl
# --request DELETE
# --header "PRIVATE-TOKEN: <your_access_token>"
# "https://gitlab.example.com/api/v4/projects/:id/repository/branches/:branch"
# ```
#
# 引数
#
# - `:id` = `project_id`
# - `:branch` = `branch_name`
#
# レスポンス
#
# - 削除した: 204
# - 失敗した: 404 `{'message': '404 Branch Not Found'}`

# +
project_id = PROJECT_ID
branch_name = "test_branch5"

# エンドポイント
url = f"{ENDPOINT}/projects/{project_id}/repository/branches/{branch_name}"

# ヘッダー
headers = {
    "PRIVATE-TOKEN": TOKEN,
}

# レスポンス
response = requests.delete(url, headers=headers)
response.raise_for_status

print(response.ok)
print(response.status_code)
response.text
# -

# # コミットAPI
#
# https://gitlab-docs.creationline.com/ee/api/commits.html

# ## コミットを確認する
#
# エンドポイント
#
# ```
# GET /projects/:id/repository/commits
# ```
#
# リクエストの例
#
# ```console
# $ curl
# --header "PRIVATE-TOKEN: <your_access_token>"
# "https://gitlab.com/api/v4/projects/:id/repository/commits"
# ```
#
# 引数
#
# - `:id` = `project_id`
# - `ref_name` = ブランチ名、タグ名、リビジョンの範囲
# - `since` =
# - `until` =
# - `path` = ファイルパス
# - `author` = コミット作成者

# +
# 引数
project_id = PROJECT_ID

# エンドポイント
url = f"{ENDPOINT}/projects/{project_id}/repository/commits"

# ヘッダー
headers = {
    "PRIVATE-TOKEN": TOKEN,
}

# クエリ
data = {"since": "2024-09-28"}

response = requests.get(url, headers=headers, data=data, timeout=10)
response.raise_for_status()

print(response.url)
print(response.ok)
print(response.status_code)
response.text
# -

# ## コミットを作成する
#
# エンドポイント
#
# ```
# POST /projects/:id/repository/commits
# ```
#
# リクエストの例
#
# ```console
# $ curl
# --request POST
# --header "PRIVATE-TOKEN: <your_access_token>"
# --header "Content-Type: application/json"
# --data "$PAYLOAD"
# "https://gitlab.example.com/api/v4/projects/1/repository/commits"
# ```  
#
# レスポンス
#
# - 成功 201
# - 失敗 400
#   - ペイロードが間違っている場合
#     - `'{"error":"actions is invalid"}'`
#   - 既存のファイルに対して`action: create`した場合
#     - `'{"message":"A file with this name already exists"}'`
#   - 存在しないファイルに対して`action: update`した場合
#     - `'{"message":"A file with this name doesn\'t exist"}'`
#
# メモ
#
# - `file_path`に作成／更新するファイルパスを指定する
#   - 拡張子も指定する
#   - 深い階層のパスを指定しても、作成してくれる

# ### コミットでできること
#
# - `id`: プロジェクトID
# - `branch`: コミットするブランチ名（既存のブランチが対象）
# - `commit_message`: コミットメッセージ
# - `start_branch`: 新しいブランチにコミットする場合
# - `author_email`: コミット作成者のメールアドレス
# - `author_name`: コミット作成者の名前
# - `stats`: `true`。コミットの統計情報

# ### アクションでできること
#
# - `action`:
#   - `create` : ファイルを作成（必須: `file_path` / `content`）
#   - `update` : ファイルを更新（必須: `file_path` / `content`）
#   - `move` : ファイルを移動（必須: `file_path` / `previous_path`）
#   - `delete` : ファイルを削除
#   - `chmod` : 権限を変更
# - `file_path`: 対象ファイルのパス
# - `previous_path`: 移動する前のファイルのパス。`move`で考慮。
# - `content`: ファイルの内容
# - `encoding`: `content`のエンコーディング（`text` or `base64`）
# - `last_commit_id`: 最後コミットID。`update` / `move` / `delete` で考慮
# - `execute_filemode`: `true` or `false`。`chmode`で考慮

# +
# 引数
project_id = PROJECT_ID
branch_name = "test_branch"

# エンドポイント
url = f"{ENDPOINT}/projects/{project_id}/repository/commits"

# ヘッダー
header = {
    "PRIVATE-TOKEN": TOKEN,
    "Content-Type": "application/json",
}

# コミットする内容
actions = [
    {
        "action": "create",
        "file_path": "test_branch.md",
        "content": "subdirectory content",
        "author_name": "gitlab-api",
    }
]

# 一度のコミットに、複数の変更を含めることができる
payload = {
    "branch": branch_name,
    "commit_message": "commit to test_branch",
    "actions": actions,
}

response = requests.post(url, headers=header, json=payload)
response.raise_for_status()

print(response.ok)
print(response.status_code)
response.json()
# -

response.text

branch_name = "test_branch2"
actions = {
    "action": "create",
    "file_path": "test_file.md",
    "content": "GitLab APIで作成したファイル",
}
create_commit(
    project_id=PROJECT_ID,
    branch_name=branch_name,
    commit_message="test commit",
    actions=actions,
    private_token=TOKEN,
)
