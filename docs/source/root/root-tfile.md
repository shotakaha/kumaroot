# TFile編

* ROOTファイルを読み込み／書き込みするためのクラス
* 読み込み／書き込みの指定が fopen などとは異なるので注意

## ファイルを読み込みたい

```cpp
TFile *fin = new TFile("input_filename", "read");
```

## ファイルを閉じたい

```cpp
fin->Close()
```

## ファイルに書き込みたい

```cpp
TFile *fout = new TFile("out.root", "recreate");
tree->Write();    // TTreeを書き込む
hist->Write();    // ヒストグラムを書き込む
canvas->Write();  // プロットを書き込む
fout->Write();    // とりあえず一切合切書き込む
```

- fout->Write("tree")ではない
- 複数のファイルを開いていた場合、どれに保存されるのだろう（※試したことない）
  - （たしか）TFileオブジェクトを作成してから、TTreeを作成しないと怒られる

## ファイルを指定して書き込みたい

```cpp
TFile fout1 = new TFile("out1.root", "recreate");
TFile fout2 = new TFile("out2.root", "recreate");

// TTree作ったり色々とする
// このままWriteすると、fout2に書き込まれる（はず）
// それを、fout1にするには、
fout1->cd();
tree->Write();
fout1->Close();
```

- cd()をすることで、fout1のディレクトリ(?)に移動する
- あんまよく分かっていないけれど、ROOTの中は、gROOTをルートとするディレクトリの構造のようになっていると思えば良い
  - その中に、TFileやら、TTreeやらといったオブジェクトがサブディレクトリのような、ファイルのような形で繋がっている
  - なので、cdをするとそのオブジェクトのディレクトリに移動できる、みたいな感じ

## 開いたファイルからヒストグラムを取ってきたい

```cpp
TFile *fin = new TFile("filename", "read");
TH1D *h1 = (TH1D*)fin->Get("h1");
```

ポイントは
- Getメソッドを使って、オブジェクトの名前を指定する
- その際、型をキャストする


### ファイルの有無を確認したい

```cpp
TString ifn = "inputfilename.root";
FileStat_t info;

if (gSystem->GetPathInfo(ifn.Data(), info)!=0) {
    printf("File '%s' does not exist.\n", ifn.Data());
} else {
    TFile *fin = new TFile(ifn.Data(), "read");
}
```

- FileStat_tという構造体の変数を使う（ファイルのサイズとかの情報を持つらしい）
- もちろん、読み込みファイルはROOTファイル以外の普通のファイルでもOK
- inputfilename.rootに関して
  - 相対パス、絶対パスでOK
  - ただし、"~/Documents/.../ifn.root"の様に、"~"でホームディレクトリを指定するのはうまくいかなかった
    - (Macなので) "/Users/username/Documents/.../ifn.root"と、絶対パスで指定したらできた
  - FileStat_tの持つ変数
    - 説明のないのはよく分かってない変数

```cpp
FileStat_t info;
info.fDev;      // デバイスID
info.fGid;      // グループID
info.fIno;      // ???
info.fIsLink;   // シンボリックリンクかどうか？（kTRUE or kFALSE）
info.fMode;     // ???
info.fMtime;    // 変更された時間
info.fSize;     // ファイルサイズ
info.fUid;      // ユーザID
info.fUrl;      // URL名（URLでなければ0が返ってくるみたい）
```


## ファイルがあった場合、それを上書きするかどうか聞くようにしたい

- 上からの派生

```cpp
if (gSystem->GetPathInfo(ofn, info)==0) {
    fprintf(stderr, "Error:\tFile '%s' already exist.\n", ofn);
    fprintf(stderr, "Error:\tDo you want to ovewrite? [y/n] > ");
    int answer, readch;
    readch = getchar();
    answer = readch;
    while (readch != '\n' && readch != EOF) readch = getchar();
    if (answer == 'y' || answer == 'Y') fprintf(stderr, "\tOverwriting '%s'.\n", ofn);
    else {
        fprintf(stderr, "\tQuit.\n");
        return 0;
    }
}
```
