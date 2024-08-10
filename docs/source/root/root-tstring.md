# 文字列したい（``TString``）

```cpp
TString str = "ROOT string"
```

``TString``は、ROOTの文字列クラスです。
C/C++の文字や文字列の扱いの面倒くささを解消してくれます。
使わない手はないでしょう、ということで紹介しておきます。

## フォーマット文字列を作りたい（``TString::Form``）

```cpp
TString str;
str.Form("Hist%d", i);
```

``TString::Form``で、``printf``と同じようにフォーマット指定子を使って文字列を作成できます。
ループ処理中にファイル名を作成したり、TTree名を作成したりする場合によく使います。

## 文字列を表示したい（``TString::Data``）

```cpp
str.Data();
```

``TString::Data``で、文字列を取得できます。

## ループ処理で複数のヒストグラムを作成したい

```cpp
const Int_t nhist = 10;
TString hname, htitle;
for (Int_t i = 0; i < nhist; i++) {
    hname.Form("h%02d", i);
    htitle.Form("%s;%s;%s", hname.Data(), "x", "y");
    h[i] = new TH1D(hname.Data(), htitle.Data(), xbin, xmin, xmax);
}
```

同じのオブジェクト名のヒストグラムは作成できません。
``hname``にループ番号を含ませることで、異なるオブジェクト名を自動生成し、複数のヒストグラムを作成しています。
