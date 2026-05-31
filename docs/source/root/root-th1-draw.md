# ヒストグラムを描画したい（`TH1::Draw`）

```cpp
h->Draw();
```

`TH1::Draw`でヒストグラムをキャンバスに描画できます。
引数に描画オプションを指定することで表示スタイルを変えられます。

```python
h.Draw()
```

| オプション | 説明 |
| --------- | ---- |
| （デフォルト） | ヒストグラム |
| `"HIST"` | アウトラインのみ |
| `"E"` | エラーバー付き |
| `"E1"` | エラーバー付き（端に横線あり） |
| `"E2"` | エラーを矩形で表示 |
| `"C"` | スプライン曲線 |
| `"L"` | 折れ線 |
| `"P"` | マーカー |
| `"BAR"` | 棒グラフ |
| `"SAME"` | 前の描画に重ねる |
| `"COLZ"` | カラーマップ（TH2向け） |

## エラーバーしたい

```cpp
h->Draw("E");

// エラーバー表示のバリエーション
h->Draw("E1");
h->Draw("E2");
```

統計誤差（ビン内容の平方根）をエラーバーで表示します。

```python
h.Draw("E")
```

## 重ね書きしたい

```cpp
h1->SetLineColor(kRed);
h1->SetFillStyle(3001);  // 斜線の塗りつぶし

h2->SetLineColor(kBlue);
h2->SetFillStyle(3002);  // 斜線の塗りつぶし

h1->Draw();
h2->Draw("SAME");
```

`"SAME"`オプションで、2つめ以降のヒストグラムを重ねて描画できます。
ヒストグラムの線の色や塗りつぶしの種類を変えておくと見分けやすくなります。

## スプライン曲線したい

```cpp
// スプライン曲線で描画
h->Draw("C");
```

`C`オプションで、ヒストグラムをスプライン曲線で描画できます。

## 折れ線したい

```cpp
// 折れ線で描画
h->Draw("L");
```

`L`オプションで、折れ線で描画できます。

## 参考資料

- [ROOT Documentation - TH1::Draw](https://root.cern/doc/master/classTH1.html)
- [ROOT Drawing Options](https://root.cern/doc/master/classTH1.html#a90c3bd37049675c14c0e06a24e18b53f)
