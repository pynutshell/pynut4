import sys, sqlite3, linecache
connect = sqlite3.connect('database.db')
cursor = connect.cursor()
for word in sys.argv[1:]:
    cursor.execute('SELECT File, Line FROM Words '
                   'WHERE Word=?', [word])
    places = cursor.fetchall()
    if not places:
         print('Word {!r} not found in index file'.format(word),
               file=sys.stderr)
         continue
    for fname, lineno in places:
        print('Word {!r} occurs in line {} of file {}:'.format(
               word,lineno,fname))
        print(linecache.getline(fname, lineno), end='')
