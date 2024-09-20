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
    const url = "SlackのURL（hooks.slack.com）";
    const data = {
        "channel" : "チャンネル名",
        "username": "通知ボットの名前",
        "attachments":[{
            //データ一式
        }],
        "icon_emoji": "絵文字コード",
    };
    // JSON形式に変換
    const payload = JSON.stringify(data);
    const options = {
        "method" : "POST",
        "contentType": "application/json",
        "payload": payload,
        "muteHttpExceptions": true
    }
    // データをSlackにPOSTする
    const response = UrlFetchApp.fetch(url, options);
    Logger.log(response);
}
```

すでに使っているSlack通知用のスクリプト``UrlFetchApp``を使っている箇所を抜粋しました。
SlackのHook用URLを作ったり、``data``にどんな値を入れられるかは、別途適切なドキュメントを参照してください。
