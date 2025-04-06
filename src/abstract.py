from abc import ABC, abstractmethod
from typing import List, Dict


class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict]:
        pass


class Storage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: 'Vacancy') -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict) -> List['Vacancy']:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: 'Vacancy') -> None:
        pass