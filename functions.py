from typing import Iterable
import re


def filter_query(param: str, data: Iterable[str]) -> Iterable[str]:
    return filter(lambda x: param in x, data)


def map_query(param: str, data: Iterable[str]) -> Iterable[str]:
    col_number = int(param)
    return map(lambda x: x.split(' ')[col_number], data)


def unique_query(data: Iterable[str], *args: str, **kwargs: str) -> Iterable[str]:
    return set(data)


def sort_query(param: str, data: Iterable[str]) -> Iterable[str]:
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]) -> Iterable[str]:
    limit = int(param)
    return list(data)[:limit]


def regex_search(param: str, data: Iterable[str]) -> Iterable[str]:
    regex = re.compile(rf"{param}")
    return regex.findall(''.join(data))
