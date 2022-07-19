def foo_child_of_bar(t):
    return t.name == 'foo' and t.parent and t.parent.name == 'bar'

soup(foo_child_of_bar)
# returns tags with name 'foo' children of tags with name 'bar'
soup.select('foo < bar')
# exactly equivalent, with no custom filter function needed
