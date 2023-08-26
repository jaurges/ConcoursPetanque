class MiniBuffer:
    def __init__(self):
        self.data = None

    def write(self, value):
        self.data = value

    def read(self):
        return self.data