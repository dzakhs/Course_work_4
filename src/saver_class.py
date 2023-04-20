from abc import ABC, abstractmethod

class Saver(ABC):

    @abstractmethod
    def add_data_hh(self, data):
        pass

    @abstractmethod
    def add_data_sj(self, data):
        pass

    @abstractmethod
    def get_data(self):
        pass



    @abstractmethod
    def delete_data(self):
        pass
