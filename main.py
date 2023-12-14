import qrcode

link = input("Please enter the website link you wish to turn into a QR Code: ")

qr = qrcode.QRCode(version=1, #Shape of the QR Code
                   error_correction=qrcode.ERROR_CORRECT_L, #Idk what this is...
                   box_size=10, 
                   border=1)

qr.add_data(link)
qr.make(fit=True) #Makes QR code fit true to size to the border

img = qr.make_image(fill_color="black", back_color="white") #Change QR Code color
img.save("QRcode.png") #Save image to project folder

