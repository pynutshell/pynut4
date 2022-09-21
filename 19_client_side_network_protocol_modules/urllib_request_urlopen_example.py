import urllib.request
unicode_url = ("https://www.unicode.org/Public"
               "/14.0.0/ucd/UnicodeData.txt")
with urllib.request.urlopen(unicode_url) as url_response:
    unicode_db = url_response.read()

print(f'{len(unicode_db):,} bytes read')
