# 状態管理したい（`state`）

```typst
// stateを作成
#let s = state("key", initial_value)

// 値を取得
#context s.get()

// 値を更新
#s.update(new_value)
#s.update(old_value => new_value)
```
