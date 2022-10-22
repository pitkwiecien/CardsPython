class FilePathError(Exception):
    def __init__(self):
        self.message = "Incorrect file path: " \
                       "directory you want to access is unreachable or you put '\\' or '/' in your file name"
        super().__init__(self.message)
