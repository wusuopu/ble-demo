#!/usr/bin/env python
# encoding: utf-8

import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)

qr.add_data('123456')
qr.make(fit=True)
img = qr.make_image()
img.save('qrcode.png')
