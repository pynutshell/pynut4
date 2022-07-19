import msvcrt
print("press z to exit, or any other key "
      "to see the key's code:")
while True:
    c = msvcrt.getch()
    if c == b'z':
        break
    print(f'{ord(c)} ({c!r})')

