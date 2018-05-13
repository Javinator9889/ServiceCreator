class NoRootPermissions(RuntimeError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class LinuxSystemNotFound(RuntimeError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class NonValidInput(RuntimeError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
