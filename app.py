from dash import Dash, dcc, html, Input, Output, callback_context
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_bootstrap_templates import load_figure_template
# from dash import dash_table
import plotly.graph_objects as go
# import base64
# import io
import tab_rb_actions
import tab_settings
import action_data_prepare
import functions
import json

# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:
# template_theme1 = "sketchy"
template_theme1 = "flatly"
template_theme2 = "darkly"
# url_theme1 = dbc.themes.SKETCHY
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[url_theme1, dbc_css])

# читаем файл с дефолтными фильтрами
# Opening JSON file
with open('saved_tab.json', 'r') as openfile:
    # Reading from json file
    saved_tab_dict = json.load(openfile)

active_tab = saved_tab_dict['tab_id']

"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H4("ОТЧЕТЫ", className="bg-primary text-white p-4 mb-2"),
                    ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2], ),

                    html.Div([
                        dcc.Tabs(
                            id="tabs-all",
                            style={
                                # 'width': '50%',
                                # 'font-size': '200%',
                                # 'height':'5vh'
                            },
                            value='user_actions_tab',
                            # parent_className='custom-tabs',
                            # className='custom-tabs-container',
                            children=[
                                tab_rb_actions.tab_rb_actions(),
                                tab_settings.tab_settings(),
                                # tab2(),
                                # tab3(),
                            ]
                        ),
                    ]),

                ]
            )
        ]
    ),
    className="m-4 dbc",
    fluid=True,
)


# Обработчик выбора квартала и года в настройках - выбор диапазона данных из основного файла.
# Возвращает заглушку - по сути переписывая csv файл actions_df_selected_by_quarter
@app.callback([
    Output('update_daterange', 'children'),
],
    [
        Input('quarter_selector', 'value'),
        Input('year_selector', 'value'),

    ],
)
def update_daterange_callback_func(quarter_selector, year_selector):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    raw_dataset = action_data_prepare.load_actions_data()
    # raw_dataset = pd.read_csv('data/2020_2021_actions.csv')
    # из вкладки Настройки берем значение из селектов "Квартал" и "Год" и получаем из них первый и последний день
    # выборки

    first_day_of_selection = functions.quarter_days(quarter_selector, year_selector)[0]
    last_day_of_selection = functions.quarter_days(quarter_selector, year_selector)[1]

    # print('first_day_of_selection', first_day_of_selection)

    actions_df_selected_by_quarter = functions.cut_df_by_dates_interval(raw_dataset, 'created_at_date',
                                                                        first_day_of_selection,
                                                                        last_day_of_selection)

    actions_df_selected_by_quarter.to_csv('data/actions_df_selected_by_quarter.csv')

    update_daterange_p = [""]

    return update_daterange_p


# Обработчик основной страницы - построения графика
@app.callback([
    Output("customer_actions_selector", "value"),
    Output("customer_actions_selector", "options"),
    Output('rb_actions_graph', 'figure'),
],
    [
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        Input('customer_actions_selector', 'value'),

        # Input('year_selector', 'value'),

    ],
)
def update_daterange(theme_selector, customer_actions_selector):
    if theme_selector:
        graph_template = 'sandstone'
        # bootstrap

    else:
        graph_template = 'plotly_dark'

    actions_df = pd.read_csv('data/actions_df_selected_by_quarter.csv')
    # action_df_groupped = actions_df.groupby(['created_at_date', 'Категория'], as_index=False).agg({'count': 'sum'})

    calendar_actions_graph_df = actions_df.groupby(['created_at_date'], as_index=False).agg({'count': 'sum'})

    checklist_customers_options_full_list = functions.action_checklist_data('сustomer')[0]
    checklist_customers_values_full_list = functions.action_checklist_data('сustomer')[1]
    if customer_actions_selector is None:
        customer_actions_selector_value = checklist_customers_values_full_list
    else:
        customer_actions_selector_value = customer_actions_selector

    actions_x = calendar_actions_graph_df['created_at_date']
    actions_y = calendar_actions_graph_df['count']

    fig_actions = go.Figure()
    fig_actions.add_trace(go.Scatter(

        x=actions_x,
        y=actions_y,
        # hoverinfo='x+y',
        mode='lines',
        # line=dict(width=0.5, color='rgb(131, 90, 241)'),
        stackgroup='one'  # define stack group
    ))
    fig_actions.update_layout(
        template=graph_template,
    )
    customer_actions_selector_options = checklist_customers_options_full_list


    return customer_actions_selector_value, customer_actions_selector_options, fig_actions


if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(host='0.0.0.0', debug=True)
