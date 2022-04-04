class natural:
    def __init__(self, str):
        self.numbers = [int(i) for i in str]
        self.digit = len(str)
    def __str__(self):
        return ''.join([str(i) for i in self.numbers])




