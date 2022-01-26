import sys, os, dbm, linecache
dbm_in = dbm.open('indexfile')
sep = os.pathsep
sep2 = sep * 2
for word in sys.argv[1:]:
    e_word = word.encode('utf-8')
    if e_word not in dbm_in:
        print('Word {!r} not found in index file'.format(word),
              file=sys.stderr)
        continue
    places = dbm_in[e_word].decode('utf-8').split(sep2)
    for place in places:
        fname, lineno = place.split(sep)
        print('Word {!r} occurs in line {} of file {}:'.format(
               word,lineno,fname))
        print(linecache.getline(fname, int(lineno)), end='')
