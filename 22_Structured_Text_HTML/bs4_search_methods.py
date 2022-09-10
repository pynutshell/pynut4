import bs4
import re

"""
For any Tag instance t and any group of positional and named arguments 
represented by ... the following equivalence always holds:

just_one = t.find(...)
other_way_list = t.find_all(..., limit=1)
other_way = other_way_list[0] if other_way_list else None
assert just_one == other_way
"""

soup = bs4.BeautifulSoup('''\
  <b foo="x"> a B tag 
    <abahh> with inner abahh </abahh>
    <foo> 
      <bb> and bb </bb> 
    </foo> 
  </b>
  <fah>foo</fah> <b>foo</b> <b>other</b>
  ''')

def child_of_foo(tag):
    return tag.parent.name == 'foo'

# search method arguments: name

soup.find_all('b') # or soup.find_all(name='b')
# returns all instances of Tag 'b' in the document

soup.find_all(['b', 'bah'])
# returns all instances of Tags 'b' and 'bah' in the document

soup.find_all(re.compile(r'^b'))
# returns all instances of Tags starting with 'b' in the document

soup.find_all(re.compile(r'bah'))
# returns all instances of Tags including string 'bah' in the document

soup.find_all(child_of_foo)
# returns all instances of Tags whose parent's name is 'foo'


# search method arguments: string

soup.find_all(string='foo')
# returns all instances of NavigableString whose text is 'foo'

soup.find_all('b', string='foo')
# returns all instances of Tag 'b' whose .string's text is 'foo'


# search method arguments: attrs

soup.find_all('b', {'foo': True, 'bar': None})
# returns all instances of Tag 'b' w/an attribute 'foo' and no 'bar'


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
