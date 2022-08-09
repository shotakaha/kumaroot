# latexmkを使いたい

LaTeX文書をコンパイルするためのMakefile的な設定ファイルだと思います。
同じディレクトリにある``latexmkrc``に設定を保存することができます。

```tex
@default_files = ("00_sample", "01_sample", "02_sample");
$pdf_mode = 4;
```
