# DAQをセットアップしたい（``rp.rp_AcqStart``）

```python
import rp

def setup_daq():

    # 初期化
    if rp.rp_IsApiInit() == 0:
        rp.rp_Init()
    rp.rp_AcqReset()

    # トリガーレベルの設定
    trigger_level = 0.5
    trigger_delay = 0
    rp.rp_AcqSetTriggerLevel(rp.RP_T_CH_1, trigger_level)
    rp.rp_AcqSetTriggerLevel(rp.RP_T_CH_2, trigger_level)
    rp.rp_AcqSetTriggerDelay(trigger_delay)

    # デシメーション設定
    rp.rp_AcqSetDecimation(rp.RP_DEC_1)

    # データ取得開始
    rp.rp_AcqStart()

    # トリガー条件の設定
    rp.rp_AcqSetTriggerSrc(rp.RP_TRIG_SRC_CHA_PE)
```

RF入力を使ってデータ取得する際に必要な要素をサンプルコードから抜粋してみました。
よくあるDAQ設定の流れに沿っているので、素直にサンプルを読めば理解できると思います。

注意点をあげるとすると、「トリガーレベルの設定」と「トリガー条件の設定は」まったく別物です。
トリガーレベルは、入力チャンネルごとに個別に設定できます。
トリガー条件は、Red Pitaya全体でひとつしか設定できません。

## リファレンス

- [Triggering with a threshold on channel](https://redpitaya.readthedocs.io/en/latest/appsFeatures/examples/acquisition/acqRF-exm1.html)
