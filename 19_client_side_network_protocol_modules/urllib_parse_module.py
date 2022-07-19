import urllib.parse as urlparse

print(urlparse.urljoin('http://host.com/some/path/here','../other/path'))
# 'http://host.com/some/other/path'

print(urlparse.urlsplit('http://www.python.org:80/faq.cgi?src=file'))
# ('http','www.python.org:80','/faq.cgi','src=file','')

print(urlparse.urlunsplit(('http','www.python.org','/faq.cgi','src=fie','')))
# 'http://www.python.org/faq.cgi?src=fie'

print(urlparse.urlsplit('http://a.com/path/a?'))
# 'http://a.com/path/a'
