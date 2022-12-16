from typing import Optional, Iterable

from werkzeug.routing import ValidationError

from functions import filter_query, map_query, unique_query, sort_query, limit_query, regex_search

# словарик с фильтрами
CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_search,
}


class WorkByFile:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self, file_name: str):
        """Читаем файл с помощью гернератора"""
        with open(file_name) as file:
            for row in file:
                yield row

    def query(self, cmd, value, data: Optional[Iterable[str]]):
        """применяем заданные фильты к файлу"""

        if cmd not in CMD_TO_FUNCTION.keys():
            raise ValidationError('cmd contains invalid value')

        if data is None:
            prepared_data = self.read_file(self.filename)
        else:
            prepared_data = data
        result = CMD_TO_FUNCTION[cmd](param=value, data=prepared_data)
        return list(result)
