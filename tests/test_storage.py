import pytest
from tempfile import TemporaryDirectory
from src.storage import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture(scope="module")
def temp_dir():
    with TemporaryDirectory() as dir_name:
        yield dir_name


@pytest.fixture
def saver(temp_dir):
    return JSONSaver(filename=f"{temp_dir}/vacancies.json")


@pytest.fixture
def vacancy():
    return Vacancy(
        title="Test Title",
        url="http://example.com",
        salary_from=50000,
        salary_to=60000,
        description="Test Description",
        requirements="Test Requirements"
    )


def test_add_vacancy(saver, vacancy):
    # Проверяем добавление вакансии
    saver.add_vacancy(vacancy)

    vacancies = saver.get_vacancies({})
    assert len(vacancies) == 1
    assert vacancies[0].title == "Test Title"


def test_get_vacancies(saver, vacancy):
    # Добавляем несколько вакансий
    saver.add_vacancy(vacancy)
    another_vacancy = Vacancy(
        title="Another Test Title",
        url="http://another.example.com",
        salary_from=70000,
        salary_to=80000,
        description="Another Test Description",
        requirements="Another Test Requirements"
    )
    saver.add_vacancy(another_vacancy)

    # Проверяем получение всех вакансий
    vacancies = saver.get_vacancies({})
    assert len(vacancies) == 2
    assert vacancies[0].title == "Test Title"
    assert vacancies[1].title == "Another Test Title"

    # Проверяем фильтрацию по критерию
    filtered_vacancies = saver.get_vacancies({"title": "Test Title"})
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].title == "Test Title"
