# HTTPリクエストしたい（``UrlFetchApp``）

```js
UrlFetchApp.fetch("URL", "オプション");
```

指定したURLに対してHTTPリクエスト（``GET``、``POST``など）できる。
コンテンツタイプやHTTPヘッダーなどはオプションで設定できる。

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
