# グループ管理したい（``GroupsApp``）

```js
const group = GroupsApp.getGroupByEmail("Googleグループのアドレス");
const users = group.getUsers();
console.log("メンバー数 = " + users.length);
```

[GroupsAppクラス](https://developers.google.com/apps-script/reference/groups/groups-app)を使って、Googleグループを管理できます。
ただし、無料のGoogleグループでは、グループメンバーの追加／削除などはできません。
