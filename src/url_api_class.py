from abc import ABC, abstractmethod


class UrlApi(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass
