# トリガーしたい（``rp_AcqGetTriggerState``）

```python
def single_daq_trigger():
    printf(f"trigger state: {rp.rp_AcqGetTriggerState()[1]}")
    printf(f"buffer state: {rp.rp_AcqGetBufferFillState()[1]}")

    while 1:
        trigger_state = rp.rp_AcqGetTriggerState()[1]
        if trigger_state == rp.RP_TRIG_STATE_TRIGGERED:
            break
    print("Triggered!")

    while 1:
        if rp.rp_AcqGetBufferFillState()[1]:
            break
    print("Data Filled!")

    printf(f"trigger state: {rp.rp_AcqGetTriggerState()[1]}")
    printf(f"buffer state: {rp.rp_AcqGetBufferFillState()[1]}")
```

トリガー条件を待つために必要な要素をサンプルコードから抜粋してみました。
基本的に``while 1``のループを使って、トリガー条件とバッファーのステータスを確認します。
ループの前後でステータスを出力してみると、それぞれでなにを確認しているかが理解できると思います。

## リファレンス

- [Triggering with a threshold on channel](https://redpitaya.readthedocs.io/en/latest/appsFeatures/examples/acquisition/acqRF-exm1.html)
