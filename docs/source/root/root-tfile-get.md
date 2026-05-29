# オブジェクトを取得したい（`TFile::Get<T>`）

```cpp
TFile *source = TFile::Open("source.root");

TTree *tree = source->Get<TTree>("events");
TH1D *h = source->Get<TH1D>("h_energy");

if (!tree) {
    std::cerr << "Failed to retrieve tree from file!" << std::endl;
    source->Close();
    return;
}

if (!h) {
    std::cerr << "Failed to retrieve histogram from file!" << std::endl;
    source->Close();
    return;
}

```

`TFile::Get<T>`は、`TFile`内のオブジェクトを名前で取得するためのテンプレートメソッドです。
`T`には、取得したいオブジェクトの型を指定します。

指定した名前のオブジェクトが存在しない場合や、型が異なる場合は`nullptr`を返します。
オブジェクトが正常に取得できたかどうかの確認に利用できます。

## オブジェクトを取得したい（`TFile::Get`）

```cpp
// C++ style
TTree *tree = dynamic_cast<TTree*>(source->Get("events"));

// C style (not recommended)
TTree *tree = (TTree*)source->Get("events");
```

`TFile::Get`は、ファイル内のオブジェクトを名前で取得するためのメソッドです（テンプレートメソッドではない）。
`TObject*`型のポインターが返ってくるため、適切な型にキャストする必要があります。

キャストの書き方には
C++スタイルの`dynamic_cast`と、
Cスタイルのキャストがあります。
C++スタイルは実行時に型の安全性をチェックするため、誤った型にキャストしようとすると`nullptr`が返されます。
Cスタイルのキャストは型の安全性をチェックがありません。
誤った型にキャストしてもコンパイルは通りますが、実行時に予期しない動作を引き起こす可能性があります。

:::{note}
ROOT5まではCスタイルのキャストが広く使われていました。
ウェブ上で見つかるコードやドキュメントではCスタイルのキャストが使われていることがあります。
ROOT6以降ではC++スタイルのキャストもしくは
`TFile::Get<T>`テンプレートメソッドの使用をオオススメします。
:::
