from typing import List
import requests
from src.abstract import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    '''реализует интерфейс VacancyAPI для работы с API HeadHunter'''
    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def __connect(self):
        '''устанавливает соединение с API'''
        response = requests.get(self.__base_url, headers=self.__headers)
        response.raise_for_status()

    def get_vacancies(self, search_query: str) -> List[dict]:
        '''отправляет запрос на получение списка вакансий по заданному запросу и параметрам'''
        self.__connect()
        params = {
            "text": search_query,
            "per_page": 100,
            "area": 113,
            "only_with_salary": True
        }
        response = requests.get(self.__base_url, headers=self.__headers, params=params)
        return response.json().get("items", [])
