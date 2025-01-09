class ComplexityAnalizerList(list):
    def __init__(self, list):
        self.extend(list)
        self.read_counter = 1

    def __getitem__(self, item):
        self.read_counter += 1
        return list.__getitem__(self, item)
    