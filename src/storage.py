import json
from pathlib import Path
from typing import List
from src.abstract import Storage
from src.vacancy import Vacancy


class JSONSaver(Storage):
    '''реализует интерфейс Storage для сохранения и загрузки вакансий в формате JSON'''
    def __init__(self, filename: str = "data/vacancies.json"):
        self.__file_path = Path(filename)
        self.__file_path.parent.mkdir(exist_ok=True)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        '''добавляет вакансию в файл, если она еще не существует'''
        data = self.__load()
        vacancy_data = {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
        if vacancy_data not in data:
            data.append(vacancy_data)
            self.__save(data)

    def get_vacancies(self, criteria: dict) -> List[Vacancy]:
        '''извлекает вакансии, соответствующие заданным критериям'''
        data = self.__load()
        return [Vacancy(**item) for item in data if all(
            item.get(k) == v for k, v in criteria.items()
        )]

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        '''удаляет вакансию из файла'''
        data = self.__load()
        vacancy_data = {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
        self.__save([item for item in data if item != vacancy_data])

    def __load(self) -> list:
        '''загружает данные из JSON-файла'''
        try:
            with self.__file_path.open('r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def __save(self, data: list):
        ''' сохраняет данные в JSON-файл'''
        with self.__file_path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
