# ファイルを読み込みたい（`TTreeReader`）

```cpp
void macro() {
    TFile *file = TFile::Open("source.root");
    if (!file || file->IsZombie()) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    // Create TTreeReader
    TTreeReader reader("events", file);

    // Set up branch readers
    // Use TTreeReaderValue<T> for single value branches
    // Use TTreeReaderArray<T> for array branches
    TTreeReaderValue<int> event_id(reader, "event_id");
    TTreeReaderValue<float> energy(reader, "energy");
    TTreeReaderArray<int> waveform(reader, "waveform");

    // Loop over entries
    // Use as iterator: reader.Next() to advance to the next entry
    while (reader.Next()) {
        // Read values with dereference operator
        int read_id = *event_id;
        float read_energy = *energy;

        // Process data...
        std::cout << "Event ID: " << read_id << ", Energy: " << read_energy << std::endl;
    }
}
```

`TTreeReader`はROOTの`TTree`を読み込むためのクラスです。
第一引数（`keyname`）に読み込む`TTree`の名前を指定します。
第二引数（`dir`）に`TFile`オブジェクトのポインターを渡します。

`TTreeReaderValue`や`TTreeReaderArray`で、各ブランチをセットアップします。
これらのメソッドはテンプレートメソッドとなっており、型安全にデータを取得できます。

`TTreeReader`オブジェクトはイテレーターのように使用でき、
`reader.Next()`を呼び出すことで、次のエントリーに進むことができます。
