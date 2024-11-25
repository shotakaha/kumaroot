# 関数したい（`function`）

```js
function 関数名(引数) {
    // 関数を定義
    const book = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = sheet.getSheetByName(引数);
    const range = sheet.getDataRange();
    const data = range.getValues()
    return data;
}
```

``function``を使って関数を定義できます。
GASプログラミングは、この関数の集合体、として作成することがほとんどです。

同じプロジェクト内で、ファイル（っぽいもの）を分けることができますが、すべてグローバル関数のように扱われます。
なので、関数名が重複しないように気をつけましょう。

JavaScriptの関数名は``camelCase``にすることが多いようですが、GASが提供する関数（``onOpen``や``onFormSubmit``など）との区別を分かりやすくするため、このドキュメントでは自作の関数は``snake_case``で書くことにします。

## 関数式したい

```js
const add = function(a, b) {
    return a + b;
}
```

関数を変数に代入できます。

## アロー関数したい

```js
const 関数名 = (引数) => 返り値;
const add = (a, b) => a + b;
```

アロー関数はES6で導入された書式です。
単純な処理は、アロー関数で書くとよいみたいです。

## map関数したい

```js
// function
const 変数 = 配列.map(function(引数) {
        処理
        return 返り値;
    });

// アロー関数
const 変数 = 配列.map(引数 => {
    処理
    return 返り値;
    });

// アロー関数（処理が1行でかける場合）
const 変数 = 配列.map(引数 => 返り値);
```

元の配列を変更せずに、新しい配列を作成できます。
新しい配列の長さは、元の配列の長さと同じです。

```js
const numbers = [1, 2, 3, 4];

// forループを使った場合
let doubled = [];
for (let i = 0; i < numbers.length; i++) {
    doubled.push(numbers[i]) * 2;
}

// mapを使った場合
const doubled = numbers.map(num => num * 2);
```

forループした場合と書き比べてみました。
単純な処理であれば、アロー関数の方がすっきり書けます。

```python
# リスト内包表記
変数 = [処理 for 引数 in 配列]
```

Pythonのリスト内包表記のようなものだと思います。

## 関数定義で思うこと

歴史的な経緯からJavaScriptには複数の関数定義があります。
後方互換性を保つことが大事にされているため、
初期から使える`function`を使った書式は、まず、体得するとよいと思います。

アロー関数はES6で新機能として導入された書式です。
利用可能な環境であれば積極的に使ってよさそうです。
ただし、あまりに複雑な処理には（可読性の観点から？）適さないようなので、従来の`function`を使った書式との使い分けを考える必要もありそうです。

## 合計したい

```js
// 配列の合計を取得
//
// - 配列の要素が数値であるかのチェックはしてない
//
// @param {number[]} numbers - 数値の配列
// @return {number} sum - 配列の合計値
function getSum(numbers) {
    let sum = 0;
    for (const n of numbers) {
        sum += n;
    }
    return sum;
}
```

JSにはビルトインのsum関数がないようなので、自分で定義します。

:::{note}

`reduce`関数を使うともっとスマートに定義できるようです。

:::

## カラムを取得したい

```js
//
// シート情報（=2次元配列）からカラム情報を取得
//
// @param {Array<Array<*>>} rows - 2次元配列（見出しなし）
// @param {Array<string>} headers - 見出し
// @param {string} name - カラム名
// @return {Array<*>} cols - 指定したカラム名の値
function getColumn(rows, headers, name) {
    // 指定したカラム名のインデックス番号を取得
    const index = headers.indexOf(name);
    const cols = rows.map(row => row[index]);
    return cols;
}
```

スプレッドシートのデータは2次元配列で読み込んで処理することが多いです。
その場合、多くのデータフレームにあるようにカラム名で該当する配列を取得できると便利だなと思ったので、自分で定義しています。

:::{note}

指定したカラム名が見出しの配列に含まれてない場合や、
データが2次元配列かどうかなどのエラーチェックを追加すると、もっと安全に利用できます。

:::
