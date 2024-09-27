# HTTPリクエストしたい（``UrlFetchApp``）

```js
UrlFetchApp.fetch("URL", "オプション");
```

`UrlFetchApp.fetch`で指定したURLに対してHTTPリクエスト（``GET``、``POST``など）できます。
コンテンツタイプやHTTPヘッダーなどはオプションできます。

## GETリクエストしたい

```js
function fetchData() {
    // URLを指定する
    const url = "https://httpbin.org/get";

    // GETリクエストを送信する
    const response = UrlFetchApp.fetch(url);

    // レスポンスの内容を取得する
    const content = response.getContentText();
    Logger.log(`content: ${content}`)
}
```

指定したURLに対してGETリクエストを送信し、レスポンスを取得するサンプルです。

## POSTリクエストしたい

```js
function postData() {
    // URLを指定する
    const url = "https://httpbin.org/post";
    // オプションを設定する
    const options = {
        "method": "post",
        "payload": {
            "key1": "value1",
            "key2": "value2"
        }
    };

    // POSTリクエストを送信する
    const response = UrlFetchApp.fetch(url, options);

    // レスポンスの内容を取得する
    const content = response.getContentText();

    Logger.log(`content: ${content}`)

}
```

指定したURLに対してPOSTリクエストを送信し、レスポンスを取得するサンプルです。
オプションで、ペイロード（＝送信するデータ）を設定できます。

## ヘッダーしたい

```js
function fetchWithHeaders() {
    // URLを指定する
    const url = "https://httpbin.org/get";

    // オプションでヘッダーを設定する
    const options = {
        "method": "get",
        "headers": {
            "Authorization": "Bearer ACCESS_TOKEN",
            "Accept": "application/json"
        }
    };

    // リクエストを送信
    const response = UrlFetchApp.fetch(url, options);

    // レスポンスの内容を取得する
    const content = response.getContentText();
    Logger.log(`content: ${content}`)

    const json = JSON.parse(content);
    Logger.log(`json: ${json}`)
}
```

`Bearer`トークンを使った認証のサンプルです。
その他のオプションは以下のとおりです。

```js
const options = {
    "method": "get",  // "post", "put", "delete"
    "headers": {},
    "payload": {},
    "muteHttpExceptions": false,
    "followRedirects": true,
    "timeoutMs": 5000,  // 5 [sec]
    "validateHttpsCertificates": true
    "contentType": "application/x-www-form-urlencoded",
    "escaping": true,
}
```

## Slackに通知したい

```js
function send_to_slack() {
    // Incoming Webhooksを有効にする
    const url = "https://hooks.slack.com/services/トークン";

    // 通知する内容
    const message = {
        "channel" : "チャンネル名",
        "username": "通知ボットの名前",
        "attachments":[{
            //データ一式
        }],
        "icon_emoji": "絵文字コード",
    };

    // 通知内容をJSON形式に変換
    const payload = JSON.stringify(message);

    // リクエストのオプション
    // POST で payloadを追加
    const options = {
        "method" : "POST",
        "contentType": "application/json",
        "payload": payload,
        "muteHttpExceptions": true
    }
    // データをSlackにPOSTする
    const response = UrlFetchApp.fetch(url, options);

    // レスポンスの内容で成功／失敗をチェックする
    const status = response.getResponseCode();
    Logger.log(`status: ${status}`);    // => 200 / 404
    const content = response.getContentText();
    Logger.log(`content: ${content}`);  // => ok  / No service
}
```

Slackの`Incoming Webhooks`アプリを使って、外部サービスからSlackに通知できるようになります。
基本となる手順は以下の通りです。

1. 通知する内容を作成する
2. JSON形式に変換する
3. POSTメソッドでリクエストを送信する

Incoming WebhooksのURLの作り方や、
``message``に追加できる値については、
それぞれ適切なドキュメントを参照してください。

## Slackのメンバー数を取得したい

```js
function getSlackMembers() {
    // Slack API Tokenをあらかじめ取得する
    // 以下のスコープが必要
    // - users:read
    // - users.read.email （アドレスを取得する場合）
    const token = "SlackのAPIトークン";

    // APIのエンドポイント -> JSON形式のデータが返ってくる
    const url = "https://slack.com/api/users.list";

    // リクエストのオプション
    // ヘッダーに認証情報を追加する
    const options = {
        "method": "get",
        "headers": {
            "Authorization": "Bearer " + token,
        }
    };

    // リクエスト
    const response = UrlFetchApp.fetch(url, options);
    const content = response.getContentText();
    const data = JSON.parse(content);

    if (data.ok) {
        const members = data.members.map(function(member) {
            const item = {
                "id": member.id,
                "name": member.name,
                "real_name": member.real_name,
                "email": member.profile.email || "no_mail",
                "is_bot": member.is_bot
            };
            return item;
            }
        );
        return members;

        // 次の forループ に相当
        // const members = [];
        // for (let i = 0; i < data.members.length; i++) {
        //    const member = data.members[i];
        //    const item = {
        //        "id": member.id,
        //        "name": member.name,
        //        "real_name": member.real_name,
        //        "email": member.profile.email || "no_mail",
        //    };
        //    members.push(item);
        //    };
        // return members;
    } else {
        Logger.log(`Error: ${data.error}`);
    };
};

function writeToSheet() {
    // 指定したスプレッドシートを取得
    const sheetId = "シートID"
    const book = SpreadsheetApp.openById(sheetId);

    // メンバー数を記録するシート
    let sheet_counter = book.getSheetByName("slackCounter");
    if (!sheet_counter){
        sheet_counter = book.insertSheet("slackCounter");
        sheet_counter.appendRow(["更新日", "メンバー数"])
    }

    // メンバー情報を記録するシート
    let sheet_roster = book.getSheetByName("slackRoster");
    if (!sheet_roster) {
        sheet_roster = book.insertSheet("slackRoster");
    }

    // Slackの情報を取得
    const members = getSlackMembers();
    if (!members || members.length === 0) {
        Logger.log("メンバー情報の取得に失敗");
        return;
    }

    // 見出し行を取得
    const headers = Object.keys(members[0]);

    // メンバー情報を2次元配列に変換
    const data = members.map(member => headers.map(header => member[header] || ""));
    //
    // 次のforループに相当
    // const data = [];
    // for (let i = 0; i < members.length; i++) {
    //     const member = members[i];
    //     const row = [];
    //     for (let j = 0; j < headers.length; j++) {
    //         const header = headers[j]
    //         const item = member[header] || ""
    //         row.push(item);
    //     }
    //     data.push(row);
    // }

    // データを出力する

    // 1. 既存のシートにメンバー数を追記する
    // 実行した時刻を最終更新日とする
    const now = new Date();
    const lastUpdated = Utilities.formatDate(now, "JST", "yyyy-MM-dd HH:mm:ssZ");
    sheet_counter.appendRow([lastUpdated, members.length]);

    // 2. 現在のメンバー情報をシートに書き出す
    // 既存のシートをクリア
    sheet_roster.clear();
    sheet_roster.appendRow(headers);
    const nrows = data.length;
    const ncols = headers.length;
    const range = sheet_roster.getRange(2, 1, nrows, ncols);
    range.setValues(data);
}
```

Slack APIトークンのスコープは以下を設定します。

- `users:read`
- `users:read.email`（メールアドレスを取得する場合

取得できるユーザー情報のサンプル

- `id`
- `name`
- `real_name`
- `is_admin`
- `is_owner`
- `is_primary_owner`
- `is_bot`
- `updated`
- `profile.email`
- `profile.real_name` (= `real_name`)
- `profile.display_name`

`data`の構造

```json
{
    "ok": true,
    "members": [
        {
            "id": "ユーザーID",
            "team_id": "ワークスペースID",
            "name": "ユーザー名",
            ...
            "profile": {
                "email": "メールアドレス",
                ...
            },
            "is_bot": false,
            ...
        },
        {
            "id": "次のユーザーID",
            ...
        }
        // 他のメンバーの情報
    ]
}
```
