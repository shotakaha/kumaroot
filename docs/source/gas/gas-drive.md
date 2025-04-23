# ドライブしたい（`DriveApp`）

```js
const folder = DriveApp.getFolderById("フォルダーID");
const files = folder.getFiles();        // FileIterator
const subFolders = folder.getFolders();    // FolderIterator
const parent = folder.getParents()

```

`DriveApp.getFolderByID`で指定したIDのフォルダを取得できます。
そのフォルダ内のアイテム（ファイルとサブフォルダ）は、それぞれ
`getFiles()`と`getFolders()`で取得できます
また、親ディレクトリは`getParents()`で取得できます。

## フォルダ内のファイルを取得したい（`getFiles`）

```js
function listAllFiles(folder) {
    const files = folder.getFiles();    // フォルダ内のファイルを FileIterator としてを取得
    while (files.hasNext()) {
        const file = files.nex();
        Logger.log(file.getName());
    }
}

const folderId = "フォルダのID";
const folder = DriveApp.getFolderById(folderId);
listAllFiles(folder);
```

`getFiles()`で、その中にあるすべてのファイルを取得できます。
ただし、戻り値が`FileIterator`となっているため、`hasNext()`と`next()`を使って、1件ずつ取り出す必要があります。

```js
function getFilesAsArray(folder) {
    const iterators = folder.getFiles();

    const files = []
    while (iterator.hasNext) {
        files.push(iterator.next());
    }
    return files;
}

const folderId = "フォルダのID";
const folder = DriveApp.getFolderById(folderId);
const files = getAllFilesAsArray(folder);
```

上記のサンプルでは`FileItereator`を配列に詰め替えています。

## サブフォルダの一覧を取得したい

```js
function listSubFolders(folder) {
    const subFolders = folder.getFolders();

    while (folders.hasNext()) {
        const sub = folders.next();
        Logger.log(sub.getName())
    }
}

const folderId = "フォルダのID";
const folder = DriveApp.getFolderById(folderId);
listSubFolders(folder);
```

`getFolders`でフォルダ内のサブフォルダをすべて取得できます。
ただし、戻り値が`FolderIterator`となっているため、`hasNext()`と`next()`を使って、1件ずつ取り出す必要があります。


## フォルダ内を再帰的に取得したい

```js
function treeFolder(folder, maxDepth, options = {}) {
    const {
        startDepth = 0,
        depth = 0,
        parentId = null
    } = options;

    if (depth > maxDepth) return [];

    const result = []
    const isVisibleDepth = depth >= startDepth;

    // フォルダ自身
    if (isVisibleDepth) {
        result.push({
            type: 'folder',
            depth,
            parentId,
            dateCreated: folder.getDateCreated(),
            dateUpdated: folder.getLastUpdated(),
            description: folder.getDescription(),
            id: folder.getId(),
            name: folder.getName(),
            owner: folder.getOwner().getEmail(),
            sharingAccess: folder.getSharingAccess(),    // 共有レベル（ANYONEなど）
            sharingPermission: folder.getSharingPermission(),    // 共有権限（VIEW | EDIT）
            url: folder.getUrl(),
            children: [],    // あとで再帰的に追加
        });
    }

    // ファイルを取得
    const files = folder.getFiles();
    const fileList = [];
    while (files.hasNext()) {
        const file = files.next();
        if (isVisibleDepth) {
            fileList.push({
                type: 'file',
                depth,
                parentId: folder.getId(),
                dateCreated: file.getDateCreated(),
                dateUpdated: file.getLastUpdated(),
                description: file.getDescription(),
                id: file.getId(),
                mimeType: file.getMimeType(),
                name: file.getName(),
                owner: file.getOwner().getEmail(),
                sharingAccess: file.getSharingAccess(),
                sharingPermission: file.getSharingPermission(),
                size: file.getSize(),
                url: file.getUrl(),
            });
        }
    }

    // サブフォルダを取得
    const subFolders = folder.getFolders();
    const folderList = [];
    while (subFolders.hasNext()) {
        const child = subFolders.next()
        const subFolder = treeFolder(child, maxDepth, {
            startDepth,
            depth: depth+1,
            parentId: folder.getId()
            });
        if (subFolder.length > 0) {
            folderList.push(...subFolder);
        }
    }

    // resultに集約
    if (isVisibleDepth) {
        result[0].children = [...fileList, ...folderList];
        return result;
    } else {
        return [...fileList, ...folderList];
    }
}

const folder = DriveApp.getFolderById("フォルダID");
const tree = treeFolder(folder, 3);
console.log(JSON.stringify(tree, null, 2));
```

指定したフォルダ内のアイテムを、再帰的に拾ってくるサンプルです。
`tree`コマンドのように、探索の深さを変更できるようにしてあります。

```js
function flattenTree(tree) {
    const flatList = [];

    // nodes: Array
    function walk(nodes) {
        for (const node of nodes) {
            const { children, ...rest } = node;
            flatList.push(rest);

            if (children && children.length > 0) {
                walk(children);
            }
        }
    }

    walk(tree);
    return flatList;
}

const folder = DriveApp.getFolderById("フォルダID");
const tree = treeFolder(folder, 3);
const flat = flattenTree(tree);

console.log(JSON.stringify(flat, null, 2));
```


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

## リファレンス

- [Class DriveApp](https://developers.google.com/apps-script/reference/drive/drive-app)
