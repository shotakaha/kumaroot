# GitLabしたい

リモートリポジトリのホスティグサービスのひとつに``GitLab``があります。
[GitLab.com](https://about.gitlab.com/)でホスティングされていて、無料で使うことができます。
GitHubと比べて、チーム開発に必要なツールが揃っていて、ドキュメントも充実しています。

## GitLab Pagesしたい

（あとで整理するので、とりあえずメモ）

- {file}``.gitlab-ci.yml``
- https://docs.gitlab.com/ee/ci/jobs/job_control.html#common-if-clauses-for-rules
- https://docs.gitlab.com/ee/ci/yaml/index.html

## Personal Access Tokenしたい（`PAT`）

1. `[設定]` -> `[Access Token]`
2. `[新しいトークンを追加]`
    - `トークン名`: わかりやすい名前を入力
    - `有効期限`: 適切に設定 （空欄にするとたぶん無期限）
    - `スコープを選択`: `api` を選択
3. `[パーソナルアクセストークンを作成]`
4. `[あなたの新しいパーソナルアクセストークン]`
  - 必要なファイルにコピペ

`Personal Access Token`（PAT）は、
APIを使った操作やアプリを利用する場合に、
サービスごとに発行する認証用のトークンです。

トークンごとにスコープ（＝権限）を設定できます。
HTTPリクエストを使ったAPI操作をする場合は、
`api`を選択する必要がありました。

:::{note}

最初は `write_repository`のみ、
次に `read_api`と`write_repository`を試したのですが、API操作できずでした。

:::

### PATを管理したい

```bash
# .env
# GitLab PAT
# expires: 2024-10-27
# scope: api
GITLAB_TOKEN=トークン
```

```python
import os
token = os.environ["GITLAB_TOKEN"]
```

PATは認証用トークンなので、ソースコードにベタ書きしてはいけません。
プロジェクトごとの`.env`などに保存し、
環境変数として呼べるようにします。

### PATを再発行したい

トークンの値をあとから確認することはできません。
コピペをミスってしまった場合などでも、再発行する必要があります。

:::{hint}

サービスのパスワード変更と異なり、
気軽に削除・再発行できるところがトークンの利便性のひとつだと思います。
万が一、トークンが漏洩してしまった場合も、即削除して無効にしてしまえばOKです。

:::

## REST APIしたい

REST APIを使って、GitLabを操作できます。

### エンドポイント

REST APIのURLの基本形は
`https://gitlab.com/api/v4/{エンドポイント}`
です。
現在は`v4`のAPIのみ利用可能です。

以下に、リモートリポジトリに対してよく使う操作とエンドポイントを整理しました。

| リソース | エンドポイント |
|---|---|
| ブランチ | `/projects/:id/repository/branches` |
| コミット | `/projects/:id/repository/commits` |
| イシュー | `/projects/:id/issues` |
| マージリクエスト | `/projects/:id/merge_requests` |

### 認証

```python
import os
import requests
token = os.environ["GITLAB_TOKEN"]

# アクセストークン
headers = {"PRIVATE-TOKEN": token}

# OAuth準拠のヘッダ
headers = {"Authorization": "Bearer " + token}

# リクエスト時にヘッダーを設定（必須）
response = requests.get(..., headers=headers, ...)
```

PATを使ってAPI認証するときのヘッダー情報です。
`PRIVATE-TOKEN`ヘッダー、もしくは
OAuth準拠の`Authorization`ヘッダーを使用します。

### プロジェクト情報を取得したい（`GET`）

```python
url = f"https://gitlab.com/api/v4/projects/{project_id}"
requests.get(url, headers=...)
```

### ファイル操作したい

```python
url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/files/{file_path}"
```

```python
# ファイルを取得
headers = {"PRIVATE-TOKEN": token}
requests.get(url, headers=...)
```

`GET`メソッドで、リポジトリにあるファイルを取得できます。

```python
# ファイルを追加
headers = {"PRIVATE-TOKEN": token}
data = {
    "branch": "main",
    "content": "ファイルの内容",
    "commit_message": "コミットメッセージ",
    "encoding": "base64"
}
# ファイルを追加
requests.post(url, headers=headers, data=data)

# ファイルを更新
requests.put(url, headers=headers, data=data)
```

`POST`と`PUT`メソッドで、リポジトリにファイル（`file_path`）を追加できます。
`data`の設定が必要です。

```python
# ファイルを削除したい
headers = {"PRIVATE-TOKEN": token}
data = {
    branch: "main",
    commit_message: "コミットメッセージ（削除した理由）",
}
requests.delete(url, headers=headers, data=data)
```

### ブランチ操作したい

```python
url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/branches"

headers = {"PRIVATE-TOKEN": token}
data = {
    "branch": 新しいブランチ名,
    "ref": ベースとなるブランチ名
}
request.put(url, headers=headers, data=data)
```

- ブランチを作成したい

### コミットしたい

```python
url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/commits

data = {
    "branch": "コミットするブランチ名",
    "commit_message": "コミットメッセージ",
    "actions": [
        {
            "action": "create",
            "file_path": "ファイルのフルパス”,
            "content": "ファイルの内容",
        },
        {
            "action": "update",
            "file_path": "...",
            "content": "ファイルの内容",
        },
        {
            "action": "delete",
            "file_path": ...,
        }
    }

requests.post(url, headers=headers, data=data)
```

### マージリクエストしたい

```python
url = f"https://gitlab.com/api/v4/projects/{project_id}/merge_requests`

headers = {"PRIVATE-TOKEN": token}
data = {
    # マージ元のブランチ名
    source_branch: "feature-branch",
    # マージ先のブランチ名
    target_branch: "main",
    title: "MRのタイトル",
    description: "MRの説明。MRの説明。MRの説明。MRの説明。",
    // MRに成功したらソースブランチを削除
    remove_source_branch: true;
}
```

## リファレンス

- [REST API - creationline inc.](https://gitlab-docs.creationline.com/ee/api/rest/index.html)
- [REST API リソース - creationline inc.](https://gitlab-docs.creationline.com/ee/api/api_resources.html)
