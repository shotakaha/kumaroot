# 変数したい（``let``）

```rust
fn main() {
    let n = 42;
    println!("{}", n);
}
```

``let 変数名``で変数を定義できます。
型は勝手に推測してくれます。
変数は基本的に不変（``immutable``）です。
後から代入した場合、コンパイルエラーになります。

## 型を指定したい

```rust
fn main() {
    let n: i32 = 42;
    println!("{}", n);
}
```

``let 変数名: 型``で型を指定して変数を定義できます。

## 変更可能な変数したい（``let mut``）

```rust
fn main() {
    let mut n: i32 = 0;
    println!("{}", n)
    n = 42;
    println!("{}", n)
}
```

``let mut 変数名（: 型）``で不変でない（``mutable``）変数を定義できます。

## 型を変更したい（``as``）

```rust
fn main() {
    let a: u8 = 13;
    let b: u32 = 7;
    let c = a as u32 + b;
    println!("{}", c);

    let t = true;
    println!("{}", t as u8);
}
```

異なる数値型の変数を計算させるとコンパイルエラーになります。
``変数名 as 型``を使って一時的に型を変換できます。

## 定数したい（``const``）

```rust
const PI: f32 = 3.14159;
```

``const 変数名``で定数を定義できます。
定数名は``UPPER_SNAKE_CASE``にします。

## 配列したい

```rust
fn main() {
    let nums: [i32; 3] = [1, 2, 3];
    println!("{:?}", nums);
    println!("{}", nums[1]);
}
```

``let 変数名: [型; 長さ]``で配列を定義できます。
配列の要素はインデックスを使って取得できます。
