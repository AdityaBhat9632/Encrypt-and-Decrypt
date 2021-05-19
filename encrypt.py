msg=input("Enter The message to be encrypted  ")
alphabet='abcdefghijklmnopqrstuvwxyz'
key=5
encrypt=''
decrypt=''
for i in msg:
    position=alphabet.find(i)
    newposition=(position+5)%26
    encrypt+=alphabet[newposition]
print(encrypt)

for i in encrypt:
    pos=alphabet.find(i)
    newpos=(pos-5)%26       
    decrypt+=alphabet[newpos]
print(decrypt)

