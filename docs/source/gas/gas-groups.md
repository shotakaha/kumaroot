# グループ管理したい（``GroupsApp``）

```js
const group = GroupsApp.getGroupByEmail("Googleグループのアドレス");
const users = group.getUsers();
console.log("メンバー数 = " + users.length);
```

[GroupsAppクラス](https://developers.google.com/apps-script/reference/groups/groups-app)を使って、Googleグループを管理できます。
ただし、無料のGoogleグループでは、グループメンバーの追加／削除などはできません。

## メンバーを確認したい

```js
function getGroupMembers(groupMail) {
    const group = GroupsApp.getGroupByEmail(groupMail);
    const users = group.getUsers();
    const n = users.length;
    Logger.log(`Found ${n} members`);
    if (n === 0 ) return [];

    const members = users.map(user => {
        Utilities.sleep(500);
        return {
            email: user.getEmail(),
            role: group.getRole(user),
        }
    })

    return members;
}

function logGroupMembers(members) {
    Logger.log(JSON.stringify(members, null, 2));
}

function showGroupMembers() {
    const members = getGroupMembers();
    logGroupMembers(members);
}
```

## グループに追加したい

```js
function addUserToGroup(email, options) {
    const {
        group = "group-name@example.com",    // googlegroupsのドメイン
    } = options;

    const group = GroupApp.getGroupByEmail(group);

    const isRegistered = group.hasUser(email);
    if (isRegistered) {
        Logger.log(`${email}はグループに登録されています`)
        return
    }

    group.addUser(email);
    Logger.log(`${email}をグループに追加しました`)
}
```

## グループから削除したい

```js
function removeUserFromGroup(email, options) {
    const {
        group = "group-name@example.com"
    } = options;
    const group = GroupApp.getGroupByEmail(group);
    const isRegistered = group.hasUser(email);
    if (!isRegistered) {
        Logger.log(`${email}はグループに登録されていません`)
    }

    group.removeUser(email);
    Logger.log(`${email}をグループから削除しました`)
}
```

## メンバー一覧をシートに保存したい

```js
// ページ上部のサンプルを再利用する
function getGroupMembers() {...};

function writeGroupMembersToSheet(members, spreadsheetId, sheetName) {
    const sheet = SpreadsheetApp.openById(spreadsheetId).getSheetByName(sheetName);
    sheet.clear();

    const now = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM-dd HH:mm:ss");
    Logger.log(`Start at ${now}`);

    // Update last-updated date
    sheet.getRange("A1").setValue("Last Updated");
    sheet.getRange("B1").setValue(now);

    // Headers
    sheet.appendRow(["users", members.length]);
    sheet.appendRow(["Role", "Email"]);

    // Data
    for (const member of members) {
        sheet.appendRow([member.role, member.email]);
    }

    // Sort
    sheet.sort(1, false);

    const end = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM-dd HH:mm:ss");
    Logger.log(`End at ${end}`);
    sheet.getRange("A1").setValue("Last Updated");
    sheet.getRange("B1").setValue(end);

    return sheet;
}

function exportGroupMembers() {
    const groupMail = "group-name@example.com";
    const bookId = "スプレッドシートのID";
    const sheetName = "シートの名前";

    const members = getGroupMembers(groupMail);
    writeGroupMembersToSheet(members, bookId, sheetName);
}
```
