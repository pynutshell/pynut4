import bs4

s = bs4.NavigableString(' some text ')

soup = bs4.BeautifulSoup()
t = soup.new_tag('foo', bar='baz')
print(t)

t.append(s)
print(t)

print(t.string.wrap(soup.new_tag('moo', zip='zaap')))
print(t)
