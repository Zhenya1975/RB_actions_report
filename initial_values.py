import datetime


def get_current_quarter_and_year():
    """Получение текущего квартала и года"""
    current_date = datetime.datetime.now()
    """текущая дата в формате datetime"""
    current_quarter = current_date.month // 4 + 1

    """номер текущего квартала"""

    current_year = current_date.year
    """Номер текущего года"""
    return current_quarter, current_year
