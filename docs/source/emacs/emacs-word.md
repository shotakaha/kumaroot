# WordでEmacsしたい

Emacsenならば、Wordを編集しているときに、うっかりEmacsキーバインドを使ってしまうことはあるあるです。
上の行に移動しようとして{kbd}``Ctrl-P``を押してしまい、印刷ダイアログを起動させた回数は数え切れません。

同じような経験をしたことがあるならば、Wordのショートカットキーをカスタマイズしてみましょう。
ちまちまと設定しなければならず、最初の手間はかかりますが、QoLが爆上がりすること間違いなしです。

## Wordのショートカットキーを変更したい

1. ``Microsoft Word``を起動する
2. ``Tools`` -> ``Customize Keyboard``をクリック
3. ダイアログで該当する操作を探し、キーを追加／削除する
   1. {guilabel}``Categories``: {guilabel}`All Commands`を選択
   2. {guilabel}``Commands``: Wordの操作名のキーワードで検索
   3. {guilabel}``Specify a Keyboard Shortcut``: 既存のキーを削除したり、新しいキーを割り当てる

macOSのWordでは、多くのショートカットキーの修飾キーは{kbd}`Ctrl`キーにも、{kbd}``Cmd``キーにもバインドされています。
なので、Emacsバインドと競合するショートカットキーであっても、{kbd}`Ctrl`キーを使うバインドのほうを削除したり、別の操作に割り当てたりしても、あまり問題は起こりません。

## 置き換えたショートカットキー

以下に、実際に置き換えた内容をリストしておきます。

| Wordの操作名 | Emacsバインド | 備考 |
|---|---|---|
| ``Cancel`` | ``C-g`` | ``C-g``を追加 |
| ``DocClose`` / ``FileExit`` | ``cmd-w`` / ``cmd-q`` |
| ``FileSave`` | ``cmd-s`` |
| ``EditUndo`` | ``cmd-z`` / ``C-/`` |
| ``CharLeft`` | ``C-b`` |
| ``CharRight`` | ``C-f`` |
| ``LineDown`` | ``C-n`` |
| ``LineUp`` | ``C-p`` |
| ``StartOfLine`` | ``C-a`` |
| ``EndOfLine`` | ``C-e`` |
| ``PageDown`` | ``C-v`` |
| ``PageUp`` | ``S-C-v`` |
| ``CmdInsNewPara`` | ``C-o`` |
| ``ApplyListBullet`` | ``cmd-S-8`` | Googleドキュメント |
| ``ApplyHeading1`` | ``cmd-option-1`` | Googleドキュメント |
| ``ApplyHeading2`` | ``cmd-option-2`` | Googleドキュメント |
| ``ApplyHeading3`` | ``cmd-option-3`` | Googleドキュメント |
| ``IndentLine`` | ``C-i`` |
| ``UnIndentLine`` | ``S-C-i`` |
| ``DeleteBackWord`` | ``C-h`` |
| ``DeleteWord`` | ``C-d`` |
| ``EditPaste`` | ``C-y`` |
| ``EditFindPrevious`` | ``C-r`` |
| ``EditFind`` | ``C-s`` |
| ``ResetChar`` | ``C-SPC`` |
| ``ShowComments`` | ``C-;`` |
| ``FileNew`` | ``cmd-o`` |
| ``EditReplace`` | ``S-C-r`` |
| ``FileNewDefault`` | ``C-x C-n`` |
