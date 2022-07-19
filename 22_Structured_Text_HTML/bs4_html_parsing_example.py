import urllib.request, urllib.parse, bs4

f = urllib.request.urlopen('http://www.python.org')
b = bs4.BeautifulSoup(f)

seen = set()
for anchor in b('a'):
    url = anchor.get('href')
    if url is None or url in seen:
        continue
    seen.add(url)
    pieces = urllib.parse.urlparse(url)
    if pieces[0] == 'http':
        print(urllib.parse.urlunparse(pieces))
