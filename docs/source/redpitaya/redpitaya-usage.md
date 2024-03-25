# Red Pitayaの使い方

```python
import rp
```

Red Pitaya内のJupyter Labを使うときは、``import rp``でAPIを使うことができます。
``rp``は、よくあるPythonのモジュールとは違って、グローバル変数のようなオブジェクトです。
``rp``オブジェクト（？）が持っている変数を、直接書き換えたり、参照することで、データが取得できます。

C言語で書かれたAPIをPythonでも使えるようになっているのですが、そこの変換ががよく分かっていません。
公式ドキュメントもあまり優しくないため、とりあえず使いながら整理します。

```{toctree}
---
maxdepth: 1
---
redpitaya-init
```


## リファレンス

- [Red Pitaya Documentation](https://redpitaya.readthedocs.io/en/latest/)
- [2.3.3 Jupyter Lab](https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/jupyter/Jupyter.html)
- [2.3.5 List of supported SCPI & API commands](https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/command_list.html)
- [2.3.6 Examples](https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/examples_top.html)
- [2.3.6.4.1 Triggering with a threshold on channel](https://redpitaya.readthedocs.io/en/latest/appsFeatures/examples/acquisition/acqRF-exm1.html)
- [Red Pitaya - GitHub](https://github.com/RedPitaya/RedPitaya)
