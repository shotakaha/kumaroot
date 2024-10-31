# メールしたい（`MailApp` / `GmailApp`）

```js
MailApp.sendEmail("メッセージオブジェクト");
MailApp.sendEmail("宛先", "件名", "本文");
MailApp.sendEmail("宛先", "件名", "本文", "オプション");
```

GASからメールするには
`MailApp`クラスを使う方法と
`GmailApp`クラスを使う方法の2通りあります。

`MailApp`は送信専用です。シンプルで使いやすいです。
下書きを作成したり、自分のメールボックス全体にアクセスしたり、
あれこれ操作したい場合は``GmailApp``を使います。

## メールしたい（`MailApp.sendEmail`）

```js
// @params {string} mailTo - 宛先アドレス
// @params {string} docId - 本文用ドキュメントのID
function send_mail(mailTo, docId) {
    const doc = DocumentApp.openById(docId);
    const mailTitle = doc.getName();
    const mailBody = doc.getBody().getText();
    const mailOption = {
        cc: "CCの宛先",
        bcc: "BCCの宛先",
        name: "送信元の名前（デフォルト：ユーザー名）",
        replyTo: "返信先アドレス（デフォルト：ユーザーのアドレス）",
        }
    MailApp.sendEmail(mailTo, mailTitle, mailBody, mailOption);
}
```

`sendEmail`でメールを送信できます。
このメソッドには複数のシグネチャがあります。
`sendEmail("宛先", "件名", "本文")`が一番直感的で使いやすいと思います。

Cc/Bccをしたい場合や、送信元の名前を変更したい場合は
`sendEmail("宛先", "件名", "本文", "オプション")`を使います。
メールの宛先（``to`` / ``cc`` / ``bcc``）は``,（カンマ）``で区切って複数指定できます。

## メールの残り回数をしりたい（`getRemainingDailyQuote`）

```js
const quota = MailApp.getRemainingDailyQuote();
Logger.info("残り回数 = " + quota);
```

1日あたりの100回の送信回数の制限があります。
`getRemainingDailyQuota`でメール送信の残り回数を確認できます。
デバッグ中は``console.log``や``Logger.info``を使って確認しながら作業するとよいです。

## スプレッドシートからデータを読み込んでメールしたい

```js
function send_mail(mailTo, sheetId, sheetName) {
    // mailTo = 宛先のアドレス
    // sheetId = GoogleプレッドシートのID
    // sheetName = シートの名前

    const sheet = SpreadsheetApp.openById(sheedId).getSheetByName(sheetName);
    const data = sheet.getDataRange().getValues();
    const mailTitle = sheet.getName();
    const mailBody = // dataをなんとかして文字列に変換する
    MailApp.sendEmail(mailTo, mailTitle, mailBody);
}
```

Googleスプレッドシートと連携することもできます。
シートの内容をメールで送信する場合を考えてみました。

## 下書きを作成したい（`GmailApp.createDraft`）

```js
// 下書きを作成する
const draft = GmailApp.createDraft("宛先", "件名", "本文", "オプション")
// メールを送信する
draft.send();

Logger.info("draft = " + draft)
// const message = draft.getMessage();
// message.getId()
// message.getDate()
// message.getTo()
// message.getCc()
// message.getBcc()
// message.getFrom()
// message.getReplyTo()
// message.getSubject()
// message.getBody()
```

``GmailApp.createDraft``でメールの下書きを作成できます。
オプションは`MailApp.sendEmail`と同じで、送信元の表示名を変更したり、
返信先アドレスを設定したりできます。

下書きを作成した段階ではメールが送信されないため、デバッグ作業に重宝します。
メールを送りたいときは``send()``します。

## リファレンス

- [Class GmailApp](https://developers.google.com/apps-script/reference/gmail/gmail-app)
- [Class MailApp](https://developers.google.com/apps-script/reference/mail/mail-app)
