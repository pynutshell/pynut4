import zipfile

with zipfile.ZipFile('archive.zip') as z:
    data = z.read('data.txt')


with zipfile.ZipFile('z.zip', 'w') as zz:
    data = 'four score\nand seven\nyears ago\n'
    zz.writestr('zinfo.zip', data)


import zipfile
with zipfile.ZipFile('z.zip') as zz:
    zz.printdir()
    for name in zz.namelist():
        print('{}: {!r}'.format(name, zz.read(name)))
