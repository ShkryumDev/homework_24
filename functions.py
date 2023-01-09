import os
from typing import Iterable, Iterator, Any, Set

from flask import request, abort

import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')


def filter_query(value: str, data: Iterator[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)  # х - строка из data, проверяем что value есть в этой строке,
    # если есть, то попадет в фильтр


def unique_query(data: Iterator[str], *args: Any, **kwargs: Any) -> set[str]:
    return set(data)


def limit_query(value: str, data: Iterator[str]) -> Iterator[str]:
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: int, data: Iterator[str]) -> Iterator[str]:
    column_number: int = int(value)
    return map(lambda x: x.split(' ')[column_number], data)


def sort_query(value: str, data: Iterator[str]) -> Iterator[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def file_name_query():
    file_path = os.path.join(DATA_DIR, 'file_name')
    if not os.path.exists(file_path):
        return abort(400)


def pattern_query(value: str, data: Iterator[str]) -> Iterator[str]:
    pattern: re.Pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)
