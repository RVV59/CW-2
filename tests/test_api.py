from src.api import HeadHunterAPI

FAKE_VACANCIES_RESPONSE = {
    "items": [
        {
            "name": "Test Vacancy 1",
            "alternate_url": "http://example.com/1",
            "salary": {"from": 50000},
            "description": "Test Description 1",
            "snippet": {"requirement": "Test Requirements 1"}
        },
        {
            "name": "Test Vacancy 2",
            "alternate_url": "http://example.com/2",
            "salary": {"from": 60000},
            "description": "Test Description 2",
            "snippet": {"requirement": "Test Requirements 2"}
        }
    ]
}


def test_headhunter_get_vacancies(monkeypatch):
    def mocked_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return FAKE_VACANCIES_RESPONSE

            # Добавили метод raise_for_status
            def raise_for_status(self):
                return None

        return MockResponse()

    monkeypatch.setattr('requests.get', mocked_get)

    hh_api = HeadHunterAPI()

    result = hh_api.get_vacancies("Python Developer")

    assert isinstance(result, list), "Результат должен быть списком"
    assert len(result) == 2, "Ожидается два элемента в результате"
    assert isinstance(result[0], dict), "Элементы списка должны быть словарями"
    assert result[0]["name"] == "Test Vacancy 1", "Проверка названия первой вакансии"
    assert result[1]["name"] == "Test Vacancy 2", "Проверка названия второй вакансии"
