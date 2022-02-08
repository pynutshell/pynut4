import sys, sqlite3, linecache
connect = sqlite3.connect('database.db')
cursor = connect.cursor()
for word in sys.argv[1:]:
    cursor.execute('SELECT File, Line FROM Words '
                   'WHERE Word=?', [word])
    places = cursor.fetchall()
    if not places:
         print(f'Word {word!r} not found in index file',
               file=sys.stderr)
         continue
    for fname, lineno in places:
        print(f'Word {word!r} occurs in line {lineno} of file {fname!r}:')
        print(linecache.getline(fname, lineno), end='')
connect.close()
