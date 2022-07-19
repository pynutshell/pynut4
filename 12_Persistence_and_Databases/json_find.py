import sys, json, dbm, linecache
with dbm.open('indexfilem') as dbm_in:
    for word in sys.argv[1:]:
        if word not in dbm_in:
             print(f'Word {word!r} not found in index file',file=sys.stderr)
             continue
        places = json.loads(dbm_in[word])
        for fname, lineno in places:
            print(f'Word {word!r} occurs in line {lineno} of file {fname!r}:')
            print(linecache.getline(fname, lineno), end='')
