# グループ管理したい（``GroupsApp``）

```js
const group = GroupsApp.getGroupByEmail("Googleグループのアドレス");
const users = group.getUsers();
console.log("メンバー数 = " + users.length);
```

[GroupsAppクラス](https://developers.google.com/apps-script/reference/groups/groups-app)を使って、Googleグループを管理できます。
ただし、無料のGoogleグループでは、グループメンバーの追加／削除などはできません。

## グループのメンバー一覧を取得したい

```js
function get_group_members(groupMail, spreadsheetId, sheetName) {
  // あるMLのメンバー一覧を取得し、指定したスプレッドシートに書き込む
  // スプレッドシートはすでに作成済み

  // groupMail = メーリングリストのアドレス
  // spreadsheetID = スプレッドシートのID
  // sheetName = シート名

  // Googlegroupsの登録メンバーを取得する
  const group = GroupsApp.getGroupByEmail(groupMail);
  const users = group.getUsers();

  // 書き込むためのスプレッドシートを開く
  const sheet = SpreadsheetApp.openById(spreadsheetId).getSheetByName(sheetName);

  // シートの内容を全て削除する
  sheet.clear();

  // 開始時刻
  const startTime = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM-dd HH:mm:ss")
  Logger.log(startTime)

  // 見出し用の列を作成する
  // 1行目: 最終更新日
  sheet.getRange("A1").setValue("Last Updated")
  sheet.getRange("B1").setValue(startTime)
  // 2行目: メンバー数
  sheet.appendRow(["users", users.length]);
  // 3行目: 見出し（Role, Email）
  sheet.appendRow(["Role", "Email"])

  // メンバーの役割（Role）とメールアドレスをシートに追加する
  // Utilities.sleepをしないと、アクセス回数が早すぎてエラーになる
  for (const user of users) {
    sheet.appendRow([group.getRole(user), user.getEmail()]);
    Utilities.sleep(500);
  }

  // ソート
  // Role列（A列）でソートする（逆順）
  // OWNER -> MEMBER -> INVITED の順番にする
  sheet.sort(1, ascending=false)

  // 終了時刻
  // 1行目の最終更新日を書き換える
  const endTime = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM-dd HH:mm:ss")
  Logger.log(endTime)
  sheet.getRange("A1").setValue("Last Updated")
  sheet.getRange("B1").setValue(endTime)

  return sheet;
}

function get_group_members_of_YOURGROUP() {
  const groupMail = "グループのアドレス";
  const ssId = "作成済みのスプレッドシートID";
  const name = "作成済みのシートID"
  sheet = writeGroupMembers(groupMail, ssId, name);
}
```
