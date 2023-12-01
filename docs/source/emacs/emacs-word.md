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

| Wordの操作名 | Wordバインド | 変更点 | Emacsバインド |
|---|---|---|---|
| ``ApplyHeading1`` | ``cmd-option-1`` | そのまま | Googleドキュメント |
| ``ApplyHeading2`` | ``cmd-option-2`` | そのまま | Googleドキュメント |
| ``ApplyHeading3`` | ``cmd-option-3`` | そのまま | Googleドキュメント |
| ``ApplyListBullet`` | ``cmd-S-L`` | ``cmd-S-8``を追加 | Googleドキュメント |
| ``Cancel`` | ``Esc`` | ``C-g``を追加 | ``C-g`` |
| ``CharLeft`` | ``Left Arrow`` | ``C-b``を追加 | ``C-b`` |
| ``CharLeftExtend`` | ``S-Left Arrow`` | ``S-C-b``を追加 | ``C-SPC`` -> ``C-b`` |
| ``CharRight`` | ``Right Arrow`` | ``C-f``を追加 | ``C-f`` |
| ``CharRightExtend`` | ``S-Right Arrow`` | ``S-C-f``を追加 | ``C-SPC`` -> ``C-f`` |
| ``CmdInsNewPara`` | なし | ``C-o``を追加 | ``C-o`` |
| ``DeleteBackWord`` | そのまま | ``C-h``を追加 | ``C-h`` |
| ``DeleteWord`` | そのまま | ``C-d``を追加 | ``C-d`` |
| ``DocClose`` | ``cmd-w`` | | |
| ``EditCopy`` | ``cmd-c`` | ``C-c``を削除 | ``M-w`` |
| ``EditCut`` | ``cmd-x`` | ``C-x``を削除 | ``C-w`` |
| ``EditFind`` | ``cmd-f`` | ``C-f``を削除、``C-s``を追加 | ``C-s`` |
| ``EditFindDialog`` | なし | ``cmd-f``を追加 | |
| ``EditFindPrevious`` | ``cmd-shift-g`` | ``C-r``を追加 | ``C-r`` |
| ``EditPaste`` | ``C-y`` | ``C-v``を削除、``C-y``を追加 | ``C-y`` |
| ``EditRedoOrRepeat`` | ``cmd-y`` | ``C-y``を削除 | ``C-u 数値 C-/`` |
| ``EditReplace`` | なし | ``S-C-r``を追加 | ``M-%`` |
| ``EditSelectAll`` | ``cmd-a`` | ``C-a``を削除 | ``C-x h`` |
| ``EditUndo`` | ``cmd-z`` | ``C-z``を削除、``C-/``を追加 | ``C-/`` |
| ``EndOfLine`` | ``End`` | ``C-e``を追加 | ``C-e`` |
| ``EndOfLineExtend`` | ``S-End`` | ``C-k``を追加 | ``C-SPC`` -> ``C-e`` |
| ``FileExit`` | ``cmd-q`` | | |
| ``FileNew`` | ``cmd-S-p`` | ``cmd-S-p``を削除 | |
| ``FileNewDefault`` | ``cmd-n`` | ``C-n``を削除 | ``C-x C-f`` |
| ``FilePrint`` | ``cmd-p`` | ``C-p``を削除 | |
| ``FileSave`` | ``cmd-s`` | ``C-s``を削除 | ``C-x C-s`` |
| ``IndentLine`` | なし | ``C-i``を追加 | ``C-i`` |
| ``LineDown`` | ``Down Arrow`` | ``C-n``を追加 | ``C-n`` |
| ``LineUp`` | ``Up Arrow`` | ``C-p``を追加 | ``C-p`` |
| ``PageDown`` | ``Page Down`` | ``C-v``を追加 | ``C-v`` |
| ``PageUp`` | ``Page Up`` | ``S-C-v``を追加 | ``M-v`` |
| ``ResetChar`` | ``C-SPC`` | | |
| ``ShowComments`` | なし | ``C-;``を追加 | ``C-;`` |
| ``StartOfLine`` | ``Home`` | ``C-a``を追加 | ``C-a`` |
| ``Underline`` | ``cmd-u`` | ``C-u``を削除 | |
| ``UnIndentLine`` | なし | ``S-C-i``を追加 | ``S-TAB`` |
