# とりあえず使いたい

```console
$ git clone https://github.com/executablebooks/mystjs-quickstart.git
$ cd mystjs-quickstart
$ myst init
$ myst start
$
```

[MyST公式のチュートリアル](https://myst-tools.org/docs/mystjs/quickstart)に沿って、クイックスタートしてみます。
GitHubにチュートリアル用のディレクトリがあるので、それをクローンして作業しています。

クローンしたディレクトリで``myst init``すると``myst.yml``が作成され、MySTプロジェクトとして使えるようになります。
``myst start``するとローカルサーバーが起動します。
ブラウザで``http://localhost:3000``を開き、ライブビューしながら修正を確認できます。

[Working with MyST Documents](https://myst-tools.org/docs/mystjs/quickstart-myst-documents)のセクションでは、PDFやLaTeXなどの文書を作成するために便利なMarkdown拡張の使い方（文書のメタ情報、ブロック要素の指定、引用と参照、画像の挿入、相互参照）を把握できます。

## メタ情報したい

文書のメタ情報はYAML形式のフロントマターで設定します。
タイトルやサブタイトル、著者（名前、所属、メールアドレス、ORCIDなど）、公開ライセンス情報、キーワード、文書の出力形式などを設定できます。

## ブロック要素したい

概要などは``part``ブロックとしてマークアップすることで、出力した文書で適切に表示できます。
ブロックにできる要素名はテンプレートの詳細で確認できます。

## 引用したい

他の論文を引用する場合にはDOIを指定します。
こうすると、論文情報が自動で挿入され、さらにページ末尾に文献リストが自動で生成されます。

## 画像を挿入したい

画像を挿入するには``figure``ディレクティブを使います。
標準的なMarkdown形式の画像挿入と比べて、キャプションやラベルなどより柔軟な設定ができます。

## 相互参照したい

相互参照は、標準的なMarkdownのリンク形式で記述できます。
相互参照先の内容は、ブラウザ上でホバーコンテンツとして表示でされます。
また、数式や画像、表などいろいろな要素に対して相互参照できます。

詳しい様子は[PhD thesis written in MyST](https://phd.row1.ca/phd)のデモを眺めてみるのがよさそうです。
