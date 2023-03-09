import qrcode

#data to encode
data = input('Enter link: ')

version = int(input('Enter the version: '))
box_size= int(input('Enter the Box size: '))

#creating an instance of QR Code Class
qr= qrcode.QRCode(version, box_size, border= 5)

#adding the link
qr.add_data(data)
qr.make(fit= True)

img= qr.make_image(fill_color= 'black', back_color= 'white')

title= input('Enter title of code')

img.save(f'path_to_be_saved{title}.png')

print('qr code generated successfully, check directory')