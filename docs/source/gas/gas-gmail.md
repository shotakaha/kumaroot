# メールしたい（`MailApp` / `GmailApp`）

```js
MailApp.sendEmail("メッセージオブジェクト");
MailApp.sendEmail("宛先", "件名", "本文");
MailApp.sendEmail("宛先", "件名", "本文", "オプション");
```

`MailApp.sendEmail`でメールを送信できます。
メールの差出人は自分のGmailアドレスです。
宛先（`to`）は`,（カンマ）`で区切って複数アドレスを指定できます。

GASでメールを制御する場合、
送信専用の`MailApp`クラスと
メールボックス操作もできる`GmailApp`クラスがあります。

送信のみであればシンプルな`MailApp`で十分です。
下書きを作成したり、自分のメールボックス全体にアクセスしたり、
あれこれ操作したい場合は``GmailApp``を使います。

## 送信オプションしたい（`MailApp.sendEmail`）

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

`sendEmail`には複数のシグネチャがあります。
Cc/Bccをしたい場合や、送信元の名前を変更したい場合は
`sendEmail("宛先", "件名", "本文", "オプション")`を使います。
メールの宛先（``to`` / ``cc`` / ``bcc``）は``,（カンマ）``で区切って複数アドレスを指定できます。

このサンプルでは、ドキュメントから本文を読み込んでいます。
読み込み先をスプレッドシートに置き換えることもできます。

## 残り回数したい（`getRemainingDailyQuote`）

```js
const quota = MailApp.getRemainingDailyQuote();
Logger.info("残り回数 = " + quota);
```

1日あたりの100回の送信回数の制限があります。
`getRemainingDailyQuota`でメール送信の残り回数を確認できます。
デバッグ中は``console.log``や``Logger.info``を使って確認しながら作業するとよいです。

## 下書きしたい（`GmailApp.createDraft`）

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
