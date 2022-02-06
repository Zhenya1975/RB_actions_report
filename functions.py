from datetime import date
from calendar import monthrange
import datetime


def cut_df_by_dates_interval(df, date_field_name, start_date, end_date):
    """Выборка в диапазоне дат. Пример: date_field_name: 'close_date',  start_date, end_date - в формате
    datetime.date """
    start_date = start_date
    end_date = end_date
    after_start_date = df.loc[:, date_field_name] >= start_date
    before_end_date = df.loc[:, date_field_name] <= end_date
    between_two_dates = after_start_date & before_end_date
    result_df = df.loc[between_two_dates]
    return result_df

def quarter_important_days(quarter_number, year):
    """quarter_important_days() получает на вход номер квартала и год. 4 и 2021. На выходе отдает первый день и
    последний запрашиваемого квартала """
    first_month_of_quarter = 3 * quarter_number - 2
    last_month_of_quarter = 3 * quarter_number
    date_of_first_day_of_quarter = date(year, first_month_of_quarter, 1)
    date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
    return date_of_first_day_of_quarter, date_of_last_day_of_quarter


def quarter_days(quarter_selector_value, year_selector_value):
    # создаем выборку по кварталу - либо по текущему по умолчанию, либо по выбранному пользователем
    current_date = datetime.datetime.now()
    """текущая дата в формате datetime"""

    today = datetime.datetime.now().date()
    """текущая дата в формате date"""

    current_quarter = round((current_date.month - 1) / 3)
    """номер текущего квартала"""

    current_year = current_date.year
    """Номер текущего года"""

    requested_quarter = quarter_selector_value
    """номер квартала из инпута на странице отчета. По умолчанию - текущий"""

    requested_year = year_selector_value
    """Номер года из инпута на странице отчета. По умолчанию - текущий"""

    if requested_year == current_year and requested_quarter == current_quarter:
        first_day_of_selection = quarter_important_days(requested_quarter, requested_year)[0]
        """Если запрошенный год и квартал равен текущему, первый день выборки - это первый день квартала"""
        last_day_of_selection = today
        """Если запрошенный год и квартал равен текущему, последний день выборки - это текущий день. Иначе -последний 
        день квартала """
    else:
        first_day_of_selection = quarter_important_days(requested_quarter, requested_year)[0]
        last_day_of_selection = quarter_important_days(requested_quarter, requested_year)[1]
    return first_day_of_selection, last_day_of_selection
