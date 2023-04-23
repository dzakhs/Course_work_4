from abc import ABC, abstractmethod

class Saver(ABC):

    @abstractmethod
    def add_data(self, data, platform):
        pass


    @abstractmethod
    def get_data(self):
        pass



    @abstractmethod
    def delete_data(self):
        pass
