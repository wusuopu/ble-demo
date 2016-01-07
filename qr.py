#!/usr/bin/env python
# encoding: utf-8

import qrcode
import json

code = {
    'lockerUUID': 'FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFF0',
    'unlockServiceUUID': 'FFFFFFFF-FFFF-4FFF-8FFF-FFFFFFFFFFF1',
    'keyCodeCharateristicUUID': 'FFFFFFFF-FFFF-4FFF-8FFF-FFFFFFFFFFF2',
    'keyCode': '123456'
}

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)

qr.add_data(json.dumps(code))
qr.make(fit=True)
img = qr.make_image()
img.save('qrcode.png')
