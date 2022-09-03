# qr code  formation
#making changes in back ground or colours

import qrcode as qr
from PIL import Image
img= qr.make("hello my dreams")
img.save("ratiqr.png")

