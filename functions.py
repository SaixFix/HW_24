from typing import Iterable
import re


def filter_query(param: str, data):
    return filter(lambda x: param in x, data)


def map_query(param: str, data: Iterable[str]):
    col_number = int(param)
    return map(lambda x: x.split(' ')[col_number], data)


def unique_query(data: Iterable[str], *args, **kwargs):
    return set(data)


def sort_query(param: str, data: Iterable[str]):
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]):
    limit = int(param)
    return list(data)[:limit]


def regex_search(param: str, data: Iterable[str]):
    regex = re.compile(rf"{param}")
    return regex.findall(data)
