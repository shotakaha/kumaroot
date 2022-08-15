# クラスを作りたい

以下のサンプルコードでやっていることは同じなので、
自分が書きやすいほうで書けばよいです。

## 実行したい内容

Slack APIを使ってワークスペースに参加しているメンバーのリストと
作成済みのチャンネルのリストを取得します。

```js
function testRun() {
    const API_TOKEN = "xxxxxxxxxx"
    const sa = new SlackAccessor(API_TOKEN);
    const members = sa.requestMembers();
    const channels = sa.requestChannels();
    // （省略）取得したデータをSpreadsheetに書き込む処理
}
```

## ``class``を使った方法

```js
class SlackAccessor {
    constructor(apiToken) {
        this.apiToken = apiToken;
    }

    requestAPI(path, params) {
        // （省略）API取得に必要な情報（URLなど）を作成する処理
        // const url = ...
        // const options = ...
        const response = UrlFetchApp.fetch(url, options)
        const data = JSON.parse(response.getContentText());
        return data;
    };

    requestMemberList() {
        const response = this.requestAPI("users.list");
        return response.members;
    }

    requestChannels() {
        const response = this.requestAPI("conversations.list");
        return response.channels;
    }
}
```

## ``prototype``を使った方法

もともとJavaScriptには「クラス」を作る機能がなく、
``prototype``という機能を使って「クラスのような」実装をしていたみたいです。
これから新しく作成するスクリプトでは、この書き方を真似する必要はないと思われます。

```js
var SlackAccessor = (function () {
    function SlackAccessor(apiToken) {
        this.APIToken = apiToken;
    }

    var p = SlackAccessor.prototype;

    // API リクエスト
    p.requestAPI = function (path, params) {
        // （省略）API用のURLとオプションを作成する
        var response = UrlFetchApp.fetch(url, options);
        var data = JSON.parse(response.getContentText());
        return data;
    };

    // メンバーリスト取得
    p.requestMembers = function () {
        var response = this.requestAPI('users.list');
        return response.members;
    });

    // チャンネル情報取得
    p.requestChannels = function () {
    var response = this.requestAPI('conversations.list');
    return response.channels;
    };
);
```
