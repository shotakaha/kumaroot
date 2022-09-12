# キーボード設定

キーボード設定は考え始めると沼ですが、誰かのパソコンをちょっと使うときやパソコンを買い替えた時の再設定を考えると、ほどほどにしておいたほうがよいと思います。
僕は次の3点を変更しています。

| 変更点 | 変更前 | 変更後 |
|---|---|---
| Controlキーを追加 | {kbd}`CapsLock` | {kbd}`Control` |
| Spotlight検索 | {kbd}`Control + Space` | {kbd}`Option + Command + Space` |
| Select next input source | {kbd}`Option + Command + Space` | {kbd}`OFF` |

Emacsでは{kbd}`Ctrl`キーをよく使います。
デフォルトのキー位置（だいたい左下）では左手の小指がとても疲れてしまうため、{kbd}`A`の隣にある{kbd}`CapsLock`を置き換えています。
{kbd}`Ctrl`と{kbd}`CapsLock`をスワップしてもよいですが、そもそも{kbd}`CapsLock`を使うことはないので

{kbd}`Contrl + Space`も欠かせないキーバインドのひとつです。
デフォルトでスポットライト検索に割り当てられているので、別のキー（{kbd}`Option` + {kbd}`Command` + {kbd}`Space`）に変更しています。
それにともなって{guilabel}`Select next input source`はOFFにしました。

## キーボード設定変更時のスクリーンショット

![](fig/mac-key01.png)

{guilabel}`CapsLock`を{guilabel}`Control`に変更

![](fig/mac-key03.png)

{guilabel}`Show spotlight search（スポットライト検索）`のショートカットキーを、デフォルトの{kbd}`Control + Space`から{kbd}`Option + Command + Space`に変更。重複するキーがあるため黄色い警告がでている。

![](fig/mac-key05.png)

変更後のスポットライト検索と重複していた
{guilabel}`Select next source in input menu` は、
これまで使ったことがなかったので無効にします
