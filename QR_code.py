import qrcode as qr
img = qr.make("https://www.youtube.com/@Lamborghini")
img.save("MYQR")
