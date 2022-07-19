import os
os.environ['HOME'] = "/u/alex"

print(os.path.expandvars('$HOME/foo/'))
