import threading
L = threading.local()
print('in main thread, setting zop to 42')
L.zop = 42

def targ():
  print('in subthread, setting zop to 23')
  L.zop = 23
  print('in subthread, zop is now', L.zop)

t = threading.Thread(target=targ)
t.start()
t.join()
print('in main thread, zop is now', L.zop)

# prints:
# in main thread, setting zop to 42
# in subthread, setting zop to 23
# in subthread, zop is now 23
# in main thread, zop is now 42
