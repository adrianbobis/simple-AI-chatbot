import json


class DataLoader:

    def __init__(self, path):

        self.path = path

        self.data = self.load()

    def load(self):

        with open(self.path, "r", encoding="utf-8") as file:

            return json.load(file)
