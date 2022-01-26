
import collections, fileinput, pickle, dbm
word_pos = collections.defaultdict(list)
for line in fileinput.input():
    pos = fileinput.filename(), fileinput.filelineno()
    for word in line.split():
        word_pos[word].append(pos)
dbm_out = dbm.open('indexfilep','n')
for word in word_pos:
    dbm_out[word] = pickle.dumps(word_pos[word],2)
dbm_out.close()
