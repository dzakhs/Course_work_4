from abc import ABC, abstractmethod

# создаем абстрактный класс для работы с Api
class UrlApi(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass
