# メールを送りたい





## 送信者を設定したい

```js
const mailTo = "宛先1,宛先2,宛先3"
const mailTitle = "件名"
const mailBody = "本文"

const draft = GmailApp.createDraft(mailTo, mailTitle, mailBody, {name: "名前"});
draft.send()
```
