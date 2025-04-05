# import json
# import os
# from typing import List, Dict, Union
# # from src.abstract import VacancyAPI
# from src.vacancy import Vacancy
#
#
# class JSONSaver:
#     def __init__(self, filename: str = "data/vacancies.json"):
#         self.__filename = filename
#         os.makedirs(os.path.dirname(filename), exist_ok=True)
#         if not os.path.exists(filename):
#             with open(filename, 'w') as f:
#                 json.dump([], f)
#
#     def __load_vacancies(self) -> List[Dict]:
#         try:
#             with open(self.__filename, 'r', encoding='utf-8') as f:
#                 return json.load(f)
#         except (FileNotFoundError, json.JSONDecodeError):
#             return []
#
#     def __save_vacancies(self, vacancies: List[Dict]) -> None:
#         """Сохраняет вакансии в файл"""
#         with open(self.__filename, 'w', encoding='utf-8') as f:
#             json.dump(vacancies, f, ensure_ascii=False, indent=2)

    # def add_vacancy(self, vacancy_data: Union[Dict, Vacancy]) -> None:
    #     """Добавляет вакансию в хранилище"""
    #     if isinstance(vacancy_data, Vacancy):
    #         vacancy_data = vacancy_data.to_dict()
    #
    #     vacancies = self.__load_vacancies()
    #
    #     # Проверяем, существует ли уже такая вакансия
    #     if not any(v.get('url') == vacancy_data.get('url') for v in vacancies):
    #         vacancies.append(vacancy_data)
    #         self.__save_vacancies(vacancies)
import json
from pathlib import Path
from typing import List
from src.abstract import Storage
from src.vacancy import Vacancy


class JSONSaver(Storage):
    def __init__(self, filename: str = "data/vacancies.json"):
        self.__file_path = Path(filename)
        self.__file_path.parent.mkdir(exist_ok=True)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        data = self.__load()
        vacancy_data = {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
        if vacancy_data not in data:
            data.append(vacancy_data)
            self.__save(data)

    def get_vacancies(self, criteria: dict) -> List[Vacancy]:
        data = self.__load()
        return [Vacancy(**item) for item in data if all(
            item.get(k) == v for k, v in criteria.items()
        )]

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        data = self.__load()
        vacancy_data = {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
        self.__save([item for item in data if item != vacancy_data])

    def __load(self) -> list:
        try:
            with self.__file_path.open('r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def __save(self, data: list):
        with self.__file_path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
