# GitLabしたい

リモートリポジトリのホスティグサービスのひとつに``GitLab``があります。
[GitLab.com](https://about.gitlab.com/)でホスティングされていて、無料で使うことができます。
GitHubと比べて、チーム開発に必要なツールが揃っていて、ドキュメントも充実しています。

## GitLab Pagesしたい

（あとで整理するので、とりあえずメモ）

- {file}``.gitlab-ci.yml``
- https://docs.gitlab.com/ee/ci/jobs/job_control.html#common-if-clauses-for-rules
- https://docs.gitlab.com/ee/ci/yaml/index.html

## GitLab APIしたい

- 基本形

`https://gitlab.com/api/v4/{エンドポイント}`

- プロジェクト情報を取得したい

`GET`
`https://gitlab.com/api/v4/projects/{プロジェクトID}`

- プロジェクト内のファイルを取得したい

`GET`
`https://gitlab.com/api/v4/projects/{プロジェクトID}/repository/files/{ファイルパス}`

- ファイルを作成／更新したい

`PUT`
`https://gitlab.com/api/v4/projects/{プロジェクトID}/repository/files/{ファイルパス}`

```js
payload = {
    branch: "main",
    content: "ファイルの内容",
    commit_message: "コミットメッセージ",
    encoding: "base64"
}
```

- ファイルを追加したい

`POST`
`https://gitlab.com/api/v4/projects/{プロジェクトID}/repository/files/{ファイルパス}`

```js
payload = {
    branch: "main",
    content: "ファイルの内容",
    commit_message: "コミットメッセージ",
    encoding: "base64"
}
```

- ファイルを削除したい

`DELETE`
`https://gitlab.com/api/v4/projects/{プロジェクトID}/repository/files/{ファイルパス}`

```js
payload = {
    branch: "main",
    commit_message: "コミットメッセージ（削除した理由）",
}
```

- ブランチを作成したい

`POST`
`https://gitlab.com/api/v4/projects/{プロジェクトID}/repository/branches`

```js
payload = {
    branch: "新しいブランチ名",
    ref: "main",
}
```

- マージリクエストしたい

`POST`
`https://gitlab.com/api/v4/projects/{プロジェクトID}/merge_requests`

```js
payload = {
    source_branch: "feature-branch",  // マージ元のブランチ名
    target_branch: "main",  // マージ先のブランチ名
    title: "MRのタイトル",
    description: "MRの説明。MRの説明。MRの説明。MRの説明。",
    remove_source_branch: true  // MR後にソースブランチを削除
}
```
