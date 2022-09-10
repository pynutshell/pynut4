import bs4

# Building and adding new nodes

s = bs4.NavigableString(' some text ')

soup = bs4.BeautifulSoup()
t = soup.new_tag('foo', bar='baz')
print(t)

t.append(s)
print(t)

print(t.string.wrap(soup.new_tag('moo', zip='zaap')))
print(t)


# Replacing and removing nodes

soup = bs4.BeautifulSoup(
       '<p>first <b>second</b> <i>third</i></p>')
i = soup.i.replace_with('last')
soup.b.append(i)
print(soup)

empty_i = soup.i.unwrap()
print(soup.b.wrap(empty_i))
print(soup.body)

soup.i.clear()
print(soup)

soup.p.decompose()
print(soup)

soup.body.decompose()
print(soup)
