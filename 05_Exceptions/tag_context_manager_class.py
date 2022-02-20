# The 'tag' class as context manager is equivalent to this code:
#
#     _normal_exit = True
#     _manager = expression
#     varname = _manager.__enter__()
#     try:
#         statement(s)
#     except:
#         _normal_exit = False
#         if not _manager.__exit_(*sys.exc_info()):
#             raise
#         # note that exception does not propagate if __exit__ returns a true value
#     finally:
#         if _normal_exit:
#             _manager.__exit__(None, None, None)

class tag(object):
    def __init__(self, tagname):
        self.tagname = tagname
    def __enter__(self):
        print(f'<{self.tagname}>', end='')
    def __exit__(self, etyp, einst, etb):
        print(f'</{self.tagname}>')

tt = tag('sometag')
with tt:
    print('some output')
