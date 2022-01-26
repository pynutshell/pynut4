import collections, fileinput, shelve
word_pos = collections.defaultdict(list)
for line in fileinput.input():
    pos = fileinput.filename(), fileinput.filelineno()
    for word in line.split():
        word_pos[word].append(pos)
sh_out = shelve.open('indexfiles','n')
sh_out.update(word_pos)
sh_out.close()
