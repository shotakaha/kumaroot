# フォームしたい（`FormApp`）

```ts
// IDで取得
const form: GoogleAppsScript.Forms.Form = FormApp.openById("FORM_ID");

// 編集URL or 回答URLで取得
const form: GoogleAppsScript.Forms.Form = FormApp.openByUrl("FORM_URL");
```

`FormApp`でGoogleフォームを操作できます。
`openById`と`openByUrl`で、スプレッドシートなどと同じように
フォームのIDもしくはURLを指定して、既存のフォームを取得できます。

```ts
const FORM_ID = PropertiesService.getScriptProperties().getProperty("FORM_ID") ?? ""
const form = FormApp.openById(FORM_ID);
```

フォームのIDをハードコードしたくない場合は、
GASのScriptPropertiesを利用するとよいです。

## フォームを作成したい（`FormApp.create`）

```ts
function createForm() {
  const form: GoogleAppsScript.Forms.Form = FormApp.create("アンケートフォーム");
  Logger.log(form.getEditUrl());
}
```

`create`メソッドで、フォームを新規作成できます。

## フォームを設定したい

```ts
function settings(form: GoogleAppsScript.Forms.Form) {
  form.setDescription("これはフォームの説明です");
  form.setCollectEmail(true);    // メールアドレスを収集
  form.setLimitOneResponsePerUser(true);    // 1人1回答に制限
}
```

## 回答を取得したい（`FormApp.getResponses`）

```ts
function getResponses(
  form: GoogleAppsScript.Forms.Form
): void {
  // すべての回答を取得
  const responses: GoogleAppsScript.Forms.FormResponse[] = form.getResponses();
  Logger.log(`回答数: ${responses.length}`);

  // 1件ずつ確認
  responses.forEach( (response: GoogleAppsScript.Forms.FormResponse) => {
    // すべての質問に対する回答を取得
    const items: GoogleAppsScript.Forms.ItemResponse[] = response.getItemResponses();
    // 質問ごとの回答を確認
    items.forEach((item: GoogleAppsScript.Forms.ItemResponse) => {
      // 記述式: string
      // チェックボックス: string[]
      const answer: string | string[] = item.getResponse();
      Logger.log(answer);
    });
  });
}
```

既存のフォームから回答を取得して表示するサンプルです。
型名を確認するとわかるように、
フォーム全体の回答は`FormResponse[]`、
個別の回答は`ItemResponse[]`として取得できます。

`FormResponse`は「1人分の回答全体」を表し、
`ItemResponse`は「各質問に対する回答」を表します。

また、質問の種類によって`ItemResponse`は、
`string`（記述式など）や
`string[]`（チェックボックスなど）になります。

## フィールドを取得したい（`FormApp.getItems()`）

```ts
const form = FormApp.openById(FORM_ID);
const items: GoogleAppsScript.Forms.Item[] = form.getItems();

for (const item of items) {
    Logger.log("%s: %s", item.getId(), item.getTitle());
}
```

`getItems`でフォームのすべてのフィールドを取得できます。
戻り値は`Item[]`で、
セクション（`PAGE_BREAK`）や説明文（`SECTION_HEADER`）も含まれます。

```ts
// テキスト形式のフィールド
const textItems = form.getItems(FormApp.ItemType.TEXT);

// ラジオボタン形式のフィールド
const mcItems = form.getItems(FormApp.ItemType.MULTIPLE_CHOICE);

// TEXT: 記述式（1行）
// PARAGRAPH_TEXT: 段落（複数行）
// MULTIPLE_CHOICE: ラジオボタン
// CHECKBOX: チェックボックス
// LIST: プルダウン
// SCALE: 均等目盛
// PAGE_BREAK: セクション区切り
// SECTION_HEADER: セクションの説明文
```

`getItems`の引数に`FormApp.ItemType`を渡すことで、
指定した種類のフィールドだけを取得できます。

## フィールドのプロパティを取得したい

```ts
const form = FormApp.openById(FORM_ID);
const items = form.getItems();

for (const item of items) {
    // フィールドID（フォーム内で一意）
    const id: number = item.getId();
    // 表示順
    const index: number = item.getIndex();
    // 質問のタイトル
    const title: string = item.getTitle();
    // 質問の説明文
    const description: string = item.getHelpText();
    // フィールドの種類
    const type = item.getType();
}
```

## フィールドの種類を取得したい（`item.getType`）

```ts
const form = FormApp.openById(FORM_ID);
const items = form.getItems();

for (const item of items){
    const type = item.getType();
    Logger.log("%s: %s", item.getTitle(), type.toString());
}
```

## フィールドIDを取得したい（`item.getId`）

```ts
const form = FormApp.openById(FORM_ID);
const items = form.getItems();

for (const item of items) {
    Logger.log("id=%s  title=%s", item.getId(), item.getTitle());
}
```

`Item.getId`で、フォーム内で一意な整数IDを取得できます。
タイトルや表示順と異なり、フィールドを編集・移動しても変わりません。

```ts
const item = form.getItemById(ITEM_ID);
if (!item) {
    Logger.log("item not found");
    return;
}
Logger.log(item.getTitle());
```

`Form.getItemById`で、指定したIDのフィールドを取得できます。
既存のフォームの構造をスプレッドシートに書き出すときに、フィールドIDを取得しておくと、全体のリストアはもちろん、必要なフィールドの更新が簡単になります。


---


```js
function onFormSubmit(e) {
    // タイムスタンプを取得する
    const ts = e.response.getTimeStamp();
    const timestamp = Utilities.formatDate(ts, "JST", "yyyy-MM-dd'T'HH:mm:ss")

    // 回答アドレスを取得する
    const mail = e.response.getRespondentEmail();

    // 回答を取得する
    const responses = e.response.getItemResponses();
    const parsed = parseResponses(responses);

    // 通知メールする
    notifyToGroup(e.response);
};

// @params {ItemResponse[]} responses - フォームの回答
// @return {string} - 「質問: 回答」の形式に変換した文字列
function parseResponses(responses) {
    // 回答を「質問名：回答」の形式に変換
    const parsed = responses.map(function(itemResponse) {
        const title = itemResponse.getItem().getTitle();
        const response = itemResponse.getResponse();
        return `${title}: ${response}`;
    }).join("\n");

    // """
    // 質問1: 回答1\n
    // 質問2: 回答2\n
    // 質問3: 回答3\n
    // """
    return parsed;
}
```

`onFormSubmit`は、回答者がフォームを送信したときにトリガーされる関数です。
引数`e`にはイベントオブジェクトが自動的に渡されます。
`e.response`は`FormResponse`オブジェクトで、この中にフォーム全般の情報がはいっています。

また、フォームの回答は`e.response.getItemResponses`で取得できる
`ItemResponse`オブジェクトの配列に入っています。

`onFormSubmit`の中に、すべての処理を書いてもよいのですが、
`e.Response.getItemResponses()`を取得して、別の関数に渡すようにしておくことで、
ユニットテストが書きやすくなります。

:::{hint}

`onFormSubmit`はフォーム送信が必要なため、テスト入力が必要です。
短時間に複数サブミットして、レート制限にかかったこともあります。
回答の処理を別の関数にすることで、ダミーデータを使ってテストできるようになります。

:::

:::{note}

ウェブ検索でヒットする記事には`e.values`で回答内容を取得できると書いてありますが、
実際に確認したら`Undefined`となりました。
メソッドの仕様変更に関する適切なドキュメントは見つけることができませんでしたが、
``itemResponses.map``して回答内容を配列にしています。

:::

:::{seealso}

``itemResponses.map(...)``している部分は、おそらくPythonのリスト内容表表記と同じことをしているはずです。

```python
responses = [itemResponse.getResponse() for itemResponse in itemResponses]
```

:::

## カスタム通知したい

```js
function onFormSubmit(e) {
    // ...
    notifyToGroup(e.response);
    notifyToSlack(e.response);
    notifyToDiscord(e.response);
}
```

フォームに入力があった場合の見落としを回避するため、
関係者にメールやSlackなどで通知したいことが多いと思います。
`onFormSubmit`と連動させることで、任意のアドレスやサービスにカスタム通知できます。

::: {seealso}

Googleフォームの共同編集者にアサインしたアカウントであれば、標準機能を使って各人で通知設定の可否を設定できます。
また、回答者には回答内容のコピーを自動で返信する機能もあります。

:::

## カスタムありがとうしたい（`setConfirmationMessage`）

```js
function set_confirmation_message() {
    const from = FormApp.getActive();
    const doc = DocumentApp.openById("ドキュメントID");
    const text = doc.getBody().getText();
    Logger.info(text);
    form.setConfirmationMessage(text)
}
```

フォーム回答後に、アンケート協力のお礼などを表示できます。
簡単なメッセージであれば、フォームの設定から編集すればOKです。
ただし、メッセージ内で改行できないため、長文には不向きです。
`setConfirmationMessage`を使うと改行を含む任意のメッセージを設定できます。

このサンプルは、
オンライン講演会の申込フォームの回答後に、
接続情報などの案内を表示したい場合に使ったものです。
URL情報などを含む長文のため、メッセージの本文はドキュメントに作成し、
それを読み込んで適用しています。
メッセージ内容を変更した場合は、再度`[実行]`して読み込ませる必要があります。

## フォームを作成したい（`create`）

```js
const form = FormApp.create("新規作成するフォーム名");
const item = form.addTextItem();
item.setTitle("名前");
item.setHelpText("名前をフルネームでご記入ください");
```

Googleフォームはブラウザ上で作成するほうが圧倒的に簡単です。
ただし、設問数が多い場合には、GASから生成する方法を知っておいても損はありません。

ここでは`FormApp.create`でフォームを新規作成しています。
また、`addTextItem`で短文回答用の質問オブジェクトを追加し、
`setTitle`で質問タイトル、
`setHelpText`で質問の説明を設定しています。

## リッカート尺度したい

```js
// @params {Form} form - Formオブジェクト
function addLikertScaleItem(form) {
    // リッカート尺度の選択肢
    const choices = [
        "5:非常に満足",
        "4:満足",
        "3:どちらでもない",
        "2:不満",
        "1:非常に不満"
    ]

    form.addMultipleChoiceItem()
        .setTitle("満足度")
        .setHelpText("イベントの満足度を5段階評価で教えてください")
        .setChoiceValues(choices)
        .setRequired(true);
    return form
}

// フォームを作成する関数
function createForm() {
    const from = FormApp.create("新規作成するフォーム名");
    const item = ...;
    // 既存のフォームに設問を追加
    addLikertScaleItem(form);
}
```

`addMultipleChoiceItem`で、ラジオボタン形式（複数の選択肢から1つの回答を選択）の設問を作成できます
選択肢に区切り文字（この場合は`:`）を入れておくと、スプレッドシートで集計するときに点数を抽出しやすくなります。

:::{note}

リッカート尺度（Likert Scale）は、アンケートなどで回答者の意見や態度を数値化して評価するための手法です。
「満足度」「理解度」などを測る際に、5段階や7段階評価で利用されることが多いです。
回答者も直感的に回答しやすく、実施者も集計しやすいのでとても便利です。

:::

## 大量の質問を作成したい（動作確認中）

```js
function createFormFromSheet() {
    // スプレッドシートを取得
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActivSheet();
    const data = sheet.getDataRange().getValues();

    // フォームを新規作成する
    const form = FormApp.create("新規作成するフォーム名");

    // ヘッダー行はスキップして各行を処理する
    for (let i = 0; i < data.length; i++ ) {
        const [title, description, method, ...choices] = data[i];

        // フォームの種類に応じて質問を追加する
        let item;
        try {
            item = form[method]();
        } catch (e) {
            Logger.log(`無効なメソッド名: ${method}`)
            continue;
            // エラーをキャッチした場合、このループはスキップして、次の行のループを開始する
        };

        // 質問のタイトルと説明を設定する
        item.setTitle(title);
        if (description) {
            item.setHelpText(description);
        }

        // 選択肢が必要なメソッドのみ設定する
        // - addMultipleChoiceItem
        // - addCheckboxItem
        // - addListItem
        // - addGridItem
        // - addCheckboxGridItem


    };
};
```

スプレッドシートからアンケート項目を読み込み、フォームを生成するサンプルです。
スプレッドーシートで項目を整理することで、抜け漏れの確認や修正が簡単になります。
大量の設問を用意する場合、とても力になると思います。

- `addCheckboxGridItem()`: チェックボックス。複数回答可。グリッド。
- `addCheckboxItem()`: チェックボックス。複数回答可。
- `addDateItem()`: 日付。
- `addDateTimeItem()`: 日時。
- `addDurationItem()`: 時間の長さ。
- `addGridItem()`: ラジオボタン。グリッド。
- `addListItem()`: プルダウン。
- `addMultipleChoiceItem()`: ラジオボタン。複数回答可。
- `addParagraphTextItem()`: テキスト。長文回答。
- `addScaleItem()`: ラジオボタン。番号付き選択肢。
- `addTextItem()`: テキスト。短文回答。
- `addTimeItem()`: 時間帯
