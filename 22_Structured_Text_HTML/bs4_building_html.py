import bs4

def mktable_with_bs4(seq_of_rows):
  tabsoup = bs4.BeautifulSoup('<table>', 'html.parser')
  tab = tabsoup.table
  for row in seq_of_rows:
    tr = tabsoup.new_tag('tr')
    tab.append(tr)
    for item in row:
      td = tabsoup.new_tag('td')
      tr.append(td)
      td.string = str(item)
  return tab

# Here is an example using the function we just defined:
example = (
  ('foo', 'g>h', 'g&h'),
  ('zip', 'zap', 'zop'),
)

print(mktable_with_bs4(example))
# prints:
# <table><tr><td>foo</td><td>g&gt;h</td><td>g&amp;h</td></tr><tr><td>zip</td><td>zap</td><td>zop</td></tr></table>
