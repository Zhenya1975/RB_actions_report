import pandas as pd


def load_actions_data():
    origin_csv_file_location = '/Users/evgenijzupanik/Downloads/rb_bmtechnics_ru.csv'

    chunk = pd.read_csv(origin_csv_file_location, chunksize=100000)
    origin_df = pd.concat(chunk)
    origin_df.to_parquet('data/rb_bmtechnics_ru_2.parquet')
    origin_df = pd.read_parquet('data/rb_bmtechnics_ru_2.parquet')
    # присвоили id как индекс
    # origin_df.set_index('id', inplace=True)
    # добавляем колонку "В каком году было событие"
    origin_df['created_at_year'] = pd.to_datetime(origin_df['created_at'], unit='s').dt.year

    # добавляем колонку "В каком квартале было событие"
    origin_df['created_at_quarter'] = pd.to_datetime(origin_df['created_at'], unit='s').dt.quarter

    # добавляем колонку "В каком месяце было событие"
    origin_df['created_at_month'] = pd.to_datetime(origin_df['created_at'], unit='s').dt.month
    # добавляем колонку "В какой дате было событие"
    origin_df['created_at_date'] = pd.to_datetime(origin_df['created_at'], unit='s').dt.date
    # добавляем колонку "В каком дне недели было событие"
    origin_df['created_at_weekday'] = pd.to_datetime(origin_df['created_at'], unit='s').dt.dayofweek + 1

    # добавляем колонку "В каком часу было событие"
    origin_df['created_at_hour'] = pd.to_datetime(origin_df['created_at'], unit='s').dt.hour + 3
    # origin_df.to_csv('data/origin_df_delete.csv')

    # удаляем строки, которые были созданы роботом, а не человеком
    origin_df.dropna(subset=['object_class'], inplace=True)

    origin_df.sort_values(['created_at_date'], inplace=True)

    df_2021_2022 = origin_df[origin_df['created_at_year'].isin([2021, 2022])]
    df_2021_2022.to_csv('data/2021_2022_actions.csv')
    # df_2021_2022.to_parquet('data/2021_2022_actions.parquet')
    # max_date_in_df = origin_df['created_at_date'].max()

    # категоризируем выборку
    # получаем список категорий
    action_categories = pd.read_csv('data/action_categories.csv')
    # джойним данные со списком категорий
    raw_action_data_with_categories = pd.merge(df_2021_2022, action_categories, on='action_template_id', how='left')
    # удаляем строки, которые не прошли
    raw_action_data_with_categories.dropna(subset=['Категория'], inplace=True)

    raw_action_data_with_categories.head(1000).to_csv('data/raw_action_data_with_categories.head(1000)_delete.csv')
    return raw_action_data_with_categories


load_actions_data()


