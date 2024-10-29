# ドライブしたい（`DriveApp`）

## ドライブ容量したい

```js
const limit = DriveApp.getStorageLimit();
const used = DriveApp.getStorageUser();
```

ユーザーのドライブ容量を確認できます。

## ファイルを共有したい（`setSharing`）

```js
const folder = DriveApp.createFolder("SharedFolder");

// リンクを知っている全員に共有
// 閲覧権限
const access = DriveApp.Access.ANYONE_WITH_LINK;
const permission = DriveApp.Permission.VIEW;
folder.setSharing(access, permission);

// 限定
// 編集権限
const access = DriveApp.Access.PRIVATE;
const permission = DriveApp.Permission.EDIT;
folder.setSharing(access, permission);
```

`setSharing`メソッドで、ファイルの共有設定を有効にできます。
引数には共有方法（`DriveApp.Access`）と
権限（`DriveApp.Permission`）を指定します。

指定できる値とその内容は
[Enum Access](https://developers.google.com/apps-script/reference/drive/access)
と
[Enum Permission](https://developers.google.com/apps-script/reference/drive/permission)
を参照してください。
