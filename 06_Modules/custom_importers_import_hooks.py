import sys, types

class ImporterAndLoader:
     '''importer and loader can be a single class'''
     fake_path = '!dummy!'
     def __init__(self, path):
         # only handle our own fake-path marker
         if path != self.fake_path:
             raise ImportError
     def find_module(self, fullname):
         # don't even try to handle any qualified module name
         if '.' in fullname:
             return None
         return self
     def create_module(self, spec):
         # create module "the default way"
         return None
     def exec_module(self, mod):
         # populate the already-initialized module
         # just print a message in this toy example
         print(f'NOTE: module {mod!r} not yet written')

sys.path_hooks.append(ImporterAndLoader)
sys.path.append(ImporterAndLoader.fake_path)

if __name__ == '__main__':      # self-test when run as main script
    import missing_module       # importing a simple *missing* module
    print(missing_module)       # ...should succeed
    print(sys.modules.get('missing_module'))  # ...should also succeed