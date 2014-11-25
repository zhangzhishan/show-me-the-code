#!/usr/bin/env python
# coding=utf-8
# author = 'huhuhushan'

import Image
import ImageFont
import ImageDraw

im = Image.open("1.png")
im.convert('RGB')
d = ImageDraw.Draw(im)
d.setink(256 + 255 + 256 * 256)
Font = ImageFont.truetype('/usr/share/fonts/truetype/limelight-elementary/Limelight.ttf',40)
imageL, imageH = im.size
#for i in range(128):
i = 20
d.text((imageL - i, imageH - 120), '1', font = Font)
im.save('new.jpeg')
