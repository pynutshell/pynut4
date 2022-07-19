"""
>>> import bs4

>>> s = bs4.NavigableString(' some text ')
>>> soup = bs4.BeautifulSoup('<html><body></body></html>', 'html.parser')

>>> t = soup.new_tag('foo', bar='baz')
>>> print(t)
<foo bar="baz"></foo>

>>> t.append(s)
>>> print(t)
<foo bar="baz"> some text </foo>

>>> print(t.string.wrap(soup.new_tag('moo', zip='zaap')))
<moo zip="zaap"> some text </moo>
>>> print(t)
<foo bar="baz"><moo zip="zaap"> some text </moo></foo>

>>> soup = bs4.BeautifulSoup(
...       '<p>first <b>second</b> <i>third</i></p>', 'html.parser')
>>> i = soup.i.replace_with('last')
>>> soup.b.append(i)
>>> print(soup)
<html><body><p>first <b>second<i>third</i></b> last</p></body></html>

>>> empty_i = soup.i.unwrap()
>>> print(soup.b.wrap(empty_i))
<i><b>secondthird</b></i>
>>> print(soup)
<html><body><p>first <i><b>secondthird</b></i> last</p></body></html>

>>> soup.i.clear()
>>> print(soup)
<html><body><p>first <i></i> last</p></body></html>
>>> soup.p.decompose()
>>> print(soup)
<html><body></body></html>
"""