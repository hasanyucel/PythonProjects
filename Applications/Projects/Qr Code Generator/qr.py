import qrcode

data = "https://github.com/hasanyucel"

qr = qrcode.make(data)
qr.save("github-qr.png")