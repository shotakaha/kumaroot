# GitLabしたい

リモートリポジトリのホスティグサービスのひとつに``GitLab``があります。
[GitLab.com](https://about.gitlab.com/)でホスティングされていて、無料で使うことができます。
GitHubと比べて、チーム開発に必要なツールが揃っていて、ドキュメントも充実しています。

## GitLab Pagesしたい

（あとで整理するので、とりあえずメモ）

- {file}``.gitlab-ci.yml``
- https://docs.gitlab.com/ee/ci/jobs/job_control.html#common-if-clauses-for-rules
- https://docs.gitlab.com/ee/ci/yaml/index.html

## GitLab PATしたい

- `[設定]` -> `[Access Token]`
- `[新しいトークンを追加]`
  - `トークン名`: わかりやすい名前を入力
  - `有効期限`: 適切に設定（空欄にすると無期限）
  - `スコープを選択`: `read_repository` もしくは `write_repository` を選択
- `[パーソナルアクセストークンを作成]`
- `[あなたの新しいパーソナルアクセストークン]`
  - 必要なファイルにコピペ

APIを使った操作やアプリを利用する場合、
サービスごとにPATを発行して、
環境変数やアプリに登録する必要があります。

PATはトークンごとにスコープ（＝権限）を設定できます。
HTTPリクエストを使ったAPI操作をする場合は、
`write_repository`を選択しておけばよいと思います。

トークンの値をあとから確認することはできません。
コピペをミスってしまった場合などでも、再発行する必要があります。

:::{hint}

サービスのパスワード変更と異なり、
気軽に削除・再発行できるところがトークンの利便性のひとつだと思います。
万が一、トークンが漏洩してしまった場合も、即削除して無効にしてしまえばOKです。

:::

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
