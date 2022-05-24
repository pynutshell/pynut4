fileob = open('xxx','wb')
while True:
    data = input('Enter some text:')
    fileob.seek(0)
    fileob.write(data.encode())
    fileob.truncate()
    fileob.flush()
