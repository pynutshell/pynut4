import shutil

ignore = shutil.ignore_patterns('.*', '*.bak')
shutil.copytree('src', 'dst', ignore=ignore)
