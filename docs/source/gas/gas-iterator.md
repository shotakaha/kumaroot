# イテレーターしたい（`GoogleAppsScript.Base.Iterator`）

```ts
function iteratorToArray<T>(
  iterator: GoogleAppsScript.Base.Iterator<T>
): T[] {
  const result: T[] = [];
  while (iterator.hasNext()) {
    result.push(iterator.next());
  }
  return result;
}

// Usage
const files = iteratorToArray(folder.getFiles());
const folders = iteratorToArray(folder.getFolders());
```

イテレーター（iterator）は、配列などのコレクション型から、要素を1つずつ順番に取り出すしくみです。
`.hasNext()`で次の要素があるかを確認し、
`.next()`で次の要素を取得し、内部のカウンターを1つ進めます。

イテレーターはメモリ使用量を少なくできますが、`.map`や`.filter`などの便利メソッドが使えません。
上記のようなイテレーターをコレクション型に変換する関数を作成しておくと便利です。

## フィルタリングしたい

```ts
function iteratorToArrayWithFilter<T>(
  iterator: GoogleAppsScript.Base.Iterator<T>,
  fn: (v: T) => boolean
): T[] {
  const result: T[] = [];
  while (iterator.hasNext()) {
    const v = iterator.next();
    if (fn(v)) result.push(v);
  }
  return result;
}

// Usage
const folder = DriveApp.getFolderById("フォルダID");

const pdfFiles = iteratorToArrayWithFilter(
  folder.getFiles(),
  file => file.getName().endsWith(".pdf")
);

pdfFiles.forEach(f => console.log(f.getName()));
```

ファイルの数が多い場合など、一度に配列に変換するとメモリを使い過ぎてしまう可能性があります。

上記のサンプルは、要素を逐次フィルタリングして、条件にマッチした要素だけ残すようにしてあります。
