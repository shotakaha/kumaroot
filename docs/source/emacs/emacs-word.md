# WordでEmacsしたい

Emacsを使っていると、Wordを編集しているときに、うっかりキーバインドを使ってしまうことがあります。
macOSの場合、``control``キーとバインドされているWordのショートカットは、``command``キーでも利用できます。
なので、Emacsバインドと競合するショートカットキーから、``control``バインドを削除すると、WordでもEmacsライクな操作ができます。

## Wordのショートカットキーを変更したい

1. ``Microsoft Word``を起動する


##

| Wordの操作名 | Emacsバインド | 備考 |
|---|---|---|
| ``Cancel`` | ``C-g`` /  ``ESC`` |
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
