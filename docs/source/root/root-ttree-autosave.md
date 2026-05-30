# イベントを自動保存したい（`TTree::AutoSave`）

```cpp
// 10000イベントごとに自動的にフラッシュ
tree->SetAutoFlush(10000);
tree->SetAutoSave(100000);

// Event loop
for (int i = 0; i < n; ++i) {
    // Acquire data
    ch1 = ...;
    ch2 = ...;

    // Fill tree
    tree->Fill();

    // AutoFlush: called every 10000 events
    // AutoSave: called every 100000 events
    // AutoSave manually
    if (i % 50000 == 0) {
        tree->AutoSave("SaveSelf");
        printf("Saved %d events...\n", i);
    }
}
```

`TTree::AutoSave`は、指定したイベント数もしくはファイルサイズごとに自動的にファイルに保存する機能です。

`TTree::SetAutoFlush`で、指定したイベント数ごとに自動的にファイルにフラッシュするように設定できます。

`TTree::SetAutoSave`で、指定したイベント数もしくはファイルサイズごとに自動的にファイルに保存するように設定できます。

:::{caution}

`TTree:Write`は、ファイルに書き込む際にTTreeの内容を完全に保存します。
イベントごとに呼び出してはいけません。
イベント数が多い場合は、`AutoSave`や`AutoFlush`を活用して、定期的にファイルに書き出すようにします。

:::
