class View:
    def __init__(self, model):
        self.model = model

    def show_data(self):
        print(self.model.data)
        return self.model.data

class Model:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]  # Sample data

