
# 安裝

```
$ npm install
$ [sudo] pip install -r ./requirements.txt
```

# 使用

```
$ python qr.py
$ open qrcode.png
```

使用 smartLockApp 掃描該圖片的 QR Code 添加 key

啟動 BlueTooth 報務，並在 smartLockApp 中點擊開鎖圖標，應該能夠看到類似如下的輸出結果，
表示 code 已經通過 BlueTooth 發送成功。

```
$ node index.js
smart lock
on -> stateChange: poweredOn
on -> advertisingStart: success
EchoCharacteristic - onUnsubscribe
EchoCharacteristic - onWriteRequest: value = 3132333435363738
```


