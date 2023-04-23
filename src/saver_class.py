from abc import ABC, abstractmethod
# создаем абстрактный класс для работы с json файлом
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
