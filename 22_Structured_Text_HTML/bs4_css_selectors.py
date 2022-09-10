import bs4

def foo_child_of_bar(t):
    return t.name == 'foo' and t.parent and t.parent.name == 'bar'

soup = bs4.BeautifulSoup('<bar>Plain <foo>bold</foo></bar>')

soup.find_all(foo_child_of_bar)
# returns tags with name 'foo' children of tags with name 'bar'

soup.select('bar > foo')
# exactly equivalent, with no custom filter function needed


###
# code to execute the above search statements and print the results of each
with open(__file__) as source:
    for line in source:
        line = line.rstrip()
        if line == "###":
            break

        print(line)
        if line.startswith("soup."):
            statement = line.partition("#")[0]
            exec(f"print({statement})", globals())
