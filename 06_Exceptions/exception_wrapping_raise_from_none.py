class FileSystemDirectory:
    def __init__(self):
        self._files = {}

    def write_file(self, filename, contents):
        self._files[filename] = contents

    def read_file(self, filename):
        try:
            return self._files[filename]
        except KeyError:
            raise FileNotFoundError(filename) from None


fs = FileSystemDirectory()

fs.write_file("romeo.txt",
              "What's in a name? That which we call a rose\n"
              "By any other name would smell as sweet")
print(fs.read_file("romeo.txt"))
print(fs.read_file("data.txt"))
