class Pathspec:
    def __init__(self, pathspec, defaultExtension = None):
        if '/' in pathspec:
            self.directory = pathspec[0:pathspec.rfind('/')]
            self.directory += '/' if not self.directory.endswith('/') else ''
            dirent = pathspec.split('/').pop()
        else:
            self.directory = ''
            dirent = pathspec

        if '.' in dirent:
            self.name, _, extension = dirent.rpartition('.')
            self.extension = '.' + extension
        else:
            self.name = dirent
            self.extension = ''

        if defaultExtension is not None and self.extension == '':
            self.extension = defaultExtension if '.' in defaultExtension else '.' + defaultExtension

        self.path = self.directory + self.name + self.extension
        self.filename = self.name + self.extension

    def __str__(self):
        return self.path
