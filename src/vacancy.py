from typing import List, Dict


class Vacancy:
    __slots__ = ('title', 'url', 'salary_from', 'salary_to', 'description', 'requirements')

    def __init__(self, title: str, url: str, salary_from: int, salary_to: int,
                 description: str, requirements: str):
        self.title = title
        self.url = url
        self.salary_from = salary_from or 0
        self.salary_to = salary_to or 0
        self.description = description
        self.requirements = requirements
        self.__validate()

    def __validate(self):
        if not self.title or not self.url:
            raise ValueError("Invalid vacancy data")

    def __lt__(self, other: 'Vacancy') -> bool:
        return self.salary_from < other.salary_from

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return (
            self.title == other.title
            and self.url == other.url
            and self.salary_from == other.salary_from
            and self.salary_to == other.salary_to
            and self.description == other.description
            and self.requirements == other.requirements
        )

    def __repr__(self):
        return f"Vacancy({self.title}, {self.url}, {self.salary_from}, {self.salary_to})"

    @classmethod
    def cast_to_object_list(cls, data: List[dict]) -> List['Vacancy']:
        return [cls(
            title=item.get('name'),
            url=item.get('alternate_url'),
            salary_from=item.get('salary', {}).get('from', 0),
            salary_to=item.get('salary', {}).get('to', 0),
            description=item.get('description', ''),
            requirements=item.get('snippet', {}).get('requirement', '')
        ) for item in data]
