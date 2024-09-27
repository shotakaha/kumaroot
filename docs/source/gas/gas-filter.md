# フィルターしたい（`filter`）

```js
const 変数名 = 配列.filter(function(要素, インデックス（オプション）, 配列（オプション）)) {
    // 条件式をここで定義
    return 条件式（true/false）;  // trueならば、変数名（＝新しい配列）に追加
}

// アロー関数
const 変数名 = 配列.filter((要素, インデックス（オプション）, 配列（オプション）) => 条件式);

const 変数名 = 配列.filter((要素, インデックス（オプション）, 配列（オプション）) => {
    // 条件式をここで定義
    return 条件式（true/false）;
    }
);

```

`filter`メソッドで、ある配列オブジェクトに対して、条件を満たす要素を抽出（フィルタリング）できます。

## 年齢で抽出したい

```js
const people = [
    { name: "Alice", age: 19},
    { name: "Bob", age: 30},
    { name: "Charlie", age: 34},
    { name: "David", age: 18},
];

// 20歳以上を抽出
let adults = people.filter(function(person) { return person >= 20});

// アロー関数
let adults = people.filter(person => person >= 20);

Logger.log(adults)
```
