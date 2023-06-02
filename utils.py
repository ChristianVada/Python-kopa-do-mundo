from exceptions import *
from datetime import datetime


def data_processing(dictionary):
    if dictionary["titles"] < 0:
        raise NegativeTitlesError

    year_cup = dictionary["first_cup"]

    format_year = int(year_cup.split("-")[0])

    if format_year < 1930 or ((format_year - 1930) % 4) != 0:
        raise InvalidYearCupError

    first_cup = dictionary["first_cup"]

    format_first_cup = int(first_cup.split("-")[0])

    possible_titles = (2023 - format_first_cup) // 4

    if possible_titles < dictionary["titles"]:
        raise ImpossibleTitlesError
