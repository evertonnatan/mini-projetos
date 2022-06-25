import qrcode


link = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_YWExZjkxMmEtZWQ2MC00NjExLWE0YjYtZmVkNjZhMTFmZmQ5%40thread.v2/0?context=%7b%22Tid%22%3a%223590422d-8e59-4036-9245-d6edd8cc0f7a%22%2c%22Oid%22%3a%22c9c39212-e4b6-4a82-a170-c8e336a72aaa%22%7d"

img = qrcode.make(link)
img.show()

'''

Créditos: Hallison do canal Programação Dinâmica (https://youtu.be/BDhSrdopl-Q) 

'''
