# タイトルしたい（`SetTitle`）

```cpp
h->SetTitle("title")
h->SetTitle("title;x;y")
```

`SetTitle(const char* title)`でグラフのタイトルを変更できます。

```cpp
h->GetTitle();
```

`GetTitle()`でタイトルを確認できます。

## 軸タイトルしたい（`SetXTitle`）

```cpp
h->SetXTitle("X軸のタイトル");
```

`SetXTitle(const char* title)`でX軸のタイトルを変更できます。
同様に
`SetYTitle`でY軸のタイトル、
`SetZTitle`でZ軸のタイトルを変更できます。

```cpp
h->GetXaxis()->GetTitle();
```

軸タイトルを確認する場合は、`GetXTitle`ではなく、
`GetXaxis`などで軸オブジェクトを取得してから
`GetTitle`する必要があります。
