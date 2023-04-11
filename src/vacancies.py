

class Vacancies:
    def __init__(self, name, url, description, requirements, salary):
        self.__name = name
        self.__url = url
        self.__description = description
        self.__salary = salary
        self.__requirements = requirements

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def description(self):
        return self.__description

    @property
    def salary(self):
        return self.__salary

    @property
    def requirements(self):
        return self.__requirements


    def __str__(self):
        return f"Название вакансии: {self.__name}\n"\
               f"Ссылка: {self.__url}\n"\
               f"Описание: {self.__description}\n"\
               f"Требования: {self.__requirements}\n"\
               f"Зарплата: {self.__salary}"

    
