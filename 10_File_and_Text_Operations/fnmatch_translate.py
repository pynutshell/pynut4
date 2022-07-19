import fnmatch, re

def fnmatchnocase(filename, pattern):
    re_pat = fnmatch.translate(pattern)
    return re.match(re_pat, filename, re.IGNORECASE)
