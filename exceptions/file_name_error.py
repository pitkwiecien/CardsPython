class FileNameError(Exception):
    def __init__(self):
        self.message = "Incorrect file name"
        super().__init__(self.message)
