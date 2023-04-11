from abc import ABC, abstractmethod

class Saver(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass
