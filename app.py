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
import actions_table
import json

# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:
# template_theme1 = "sketchy"
template_theme1 = "flatly"
template_theme2 = "darkly"
# url_theme1 = dbc.themes.SKETCHY
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

available_graph_templates: ['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark',
                            'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']

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
                    ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                    # ThemeSwitchAIO(aio_id="theme", themes=[url_theme2, url_theme1]),

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



# Обработчик основной страницы - построения графика
@app.callback([
    Output("customer_actions_selector", "value"),
    Output("customer_actions_selector", "options"),
    Output("deal_actions_selector", "value"),
    Output("deal_actions_selector", "options"),
    Output("calendar_actions_selector", "value"),
    Output("calendar_actions_selector", "options"),
    Output("fleet_actions_selector", "value"),
    Output("fleet_actions_selector", "options"),
    Output("accordion_customers", "title"),
    Output("accordion_deals", "title"),
    Output("accordion_calendar", "title"),
    Output("accordion_fleet", "title"),
    Output('rb_actions_graph', 'figure'),
    Output('user_actions_table', 'children'),

],
    [
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        Input('update_dataset_btn', 'n_clicks'),
        Input('quarter_selector', 'value'),
        Input('year_selector', 'value'),
        Input('input_csv_url', 'value'),
        Input('customer_actions_selector', 'value'),
        Input('select_all_customer_actions', 'n_clicks'),
        Input('release_all_customer_actions', 'n_clicks'),
        Input('deal_actions_selector', 'value'),
        Input('select_all_deal_actions', 'n_clicks'),
        Input('release_all_deal_actions', 'n_clicks'),
        Input('calendar_actions_selector', 'value'),
        Input('select_all_calendar_actions', 'n_clicks'),
        Input('release_all_calendar_actions', 'n_clicks'),
        Input('fleet_actions_selector', 'value'),
        Input('select_all_fleet_actions', 'n_clicks'),
        Input('release_all_fleet_actions', 'n_clicks'),

        # Input('year_selector', 'value'),

    ],
)
def actions_page(theme_selector, update_dataset, quarter_selector, year_selector, input_csv_url, customer_actions_selector, select_all_customer_actions,
                 release_all_customer_actions,
                 deal_actions_selector, select_all_deal_actions, release_all_deal_actions, calendar_actions_selector,
                 select_all_calendar_actions, release_all_calendar_actions, fleet_actions_selector,
                 select_all_fleet_actions, release_all_fleet_actions):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]

    actions_df = pd.read_csv('data/actions_df_selected_by_quarter.csv')
    if theme_selector:
        graph_template = 'seaborn'
        # bootstrap

    else:
        graph_template = 'plotly_dark'

    if "update_dataset_btn" in changed_id:
        if input_csv_url == None:
            raw_df = pd.read_csv('data/2021_2022_actions.csv')
        else:
            raw_df = pd.read_csv(input_csv_url)
        actions_df = action_data_prepare.load_actions_data(raw_df, quarter_selector, year_selector)



    # actions_df = pd.read_csv(input_csv_url)
    # if input_csv_url == None:
    #     actions_df = pd.read_csv('data/actions_df_selected_by_quarter.csv')
    # else:
    #     actions_df = pd.read_csv(input_csv_url)
    # pd.read_csv('data/actions_df_selected_by_quarter.csv')
    # action_df_groupped = actions_df.groupby(['created_at_date', 'Категория'], as_index=False).agg({'count': 'sum'})

    ############ ЧЕК-ЛИСТ ДЕЙСТВИЙ В РАЗДЕЛЕ КЛИЕНТЫ #############################################
    checklist_customers_options_full_list = functions.action_checklist_data(actions_df, 'сustomer')[0]
    checklist_customers_values_full_list = functions.action_checklist_data(actions_df, 'сustomer')[1]

    if customer_actions_selector is None:
        customer_actions_selector_value = checklist_customers_values_full_list
    else:
        customer_actions_selector_value = customer_actions_selector
    # Обработчик кнопок Снять / Выбрать в блоке Клиенты
    id_select_all_customer_actions_button = "select_all_customer_actions"
    id_release_all_customer_actions_button = "release_all_customer_actions"

    # при клике на кнопку Выбрать все - выбираем все и наоборот
    if id_select_all_customer_actions_button in changed_id:
        customer_actions_selector_value = checklist_customers_values_full_list
    elif id_release_all_customer_actions_button in changed_id:
        customer_actions_selector_value = []

    ############ ЧЕК-ЛИСТ ДЕЙСТВИЙ В РАЗДЕЛЕ СДЕЛКИ ##########################################
    checklist_deals_options_full_list = functions.action_checklist_data(actions_df, 'deal')[0]
    checklist_deals_values_full_list = functions.action_checklist_data(actions_df, 'deal')[1]
    # print('checklist_deals_values_full_list', checklist_deals_values_full_list)

    if deal_actions_selector is None:
        deal_actions_selector_value = checklist_deals_values_full_list
    else:
        deal_actions_selector_value = deal_actions_selector

    # Обработчик кнопок Снять / Выбрать в блоке Сделки
    id_select_all_deals_actions_button = "select_all_deal_actions"
    id_release_all_deals_actions_button = "release_all_deal_actions"

    # при клике на кнопку Выбрать все - выбираем все и наоборот
    if id_select_all_deals_actions_button in changed_id:
        deal_actions_selector_value = checklist_deals_values_full_list
    elif id_release_all_deals_actions_button in changed_id:
        deal_actions_selector_value = []

    ############ ЧЕК-ЛИСТ ДЕЙСТВИЙ В РАЗДЕЛЕ КАЛЕНДАРЬ ##########################################
    checklist_calendar_options_full_list = functions.action_checklist_data(actions_df, 'calendar')[0]
    checklist_calendar_values_full_list = functions.action_checklist_data(actions_df, 'calendar')[1]
    # print('checklist_deals_values_full_list', checklist_deals_values_full_list)

    if calendar_actions_selector is None:
        calendar_actions_selector_value = checklist_calendar_values_full_list
    else:
        calendar_actions_selector_value = calendar_actions_selector

    # Обработчик кнопок Снять / Выбрать в блоке Календарь
    id_select_all_calendar_actions_button = "select_all_calendar_actions"
    id_release_all_calendar_actions_button = "release_all_calendar_actions"

    # при клике на кнопку Выбрать все - выбираем все и наоборот
    if id_select_all_calendar_actions_button in changed_id:
        calendar_actions_selector_value = checklist_calendar_values_full_list
    elif id_release_all_calendar_actions_button in changed_id:
        calendar_actions_selector_value = []

    ############ ЧЕК-ЛИСТ ДЕЙСТВИЙ В РАЗДЕЛЕ ПАРК ТЕХНИКИ ##########################################
    checklist_fleet_options_full_list = functions.action_checklist_data(actions_df, 'fleet')[0]
    checklist_fleet_values_full_list = functions.action_checklist_data(actions_df, 'fleet')[1]

    if fleet_actions_selector is None:
        fleet_actions_selector_value = checklist_fleet_values_full_list
    else:
        fleet_actions_selector_value = fleet_actions_selector

    # Обработчик кнопок Снять / Выбрать в блоке Парк техники
    id_select_all_fleet_actions_button = "select_all_fleet_actions"
    id_release_all_fleet_actions_button = "release_all_fleet_actions"

    # при клике на кнопку Выбрать все - выбираем все и наоборот
    if id_select_all_fleet_actions_button in changed_id:
        fleet_actions_selector_value = checklist_fleet_values_full_list
    elif id_release_all_fleet_actions_button in changed_id:
        fleet_actions_selector_value = []

    ############# ПРИМЕНЕНИЕ ФИЛЬТРОВ ######################
    actions_df = actions_df.loc[(actions_df['action_template_id'].isin(customer_actions_selector_value)) |
                                (actions_df['action_template_id'].isin(deal_actions_selector_value)) |
                                (actions_df['action_template_id'].isin(calendar_actions_selector_value)) |
                                (actions_df['action_template_id'].isin(fleet_actions_selector_value))
                                ]
    # print('длина датафрейма после применения фильтров', len(actions_df))

    fig_actions = go.Figure()
    fig_actions.update_layout(
        title="Действия пользователей, кол-во",

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

    ################## ГРАФИК КЛИЕНТЫ ###########################
    actions_customers_df = actions_df.loc[(actions_df['action_category'] == 'сustomer')]
    # print('длина датафрейма customer в графике', len(actions_customers_df))
    number_of_customers_actions = actions_customers_df['count'].sum()
    customer_actions_graph_df = actions_customers_df.groupby(['created_at_date'], as_index=False).agg({'count': 'sum'})
    actions_x = customer_actions_graph_df['created_at_date']
    actions_customer_y = customer_actions_graph_df['count']

    fig_actions.add_trace(go.Scatter(

        x=actions_x,
        y=actions_customer_y,
        name='Клиенты',
        # hoverinfo='x+y',
        mode='lines',
        # line=dict(width=0.5, color='rgb(131, 90, 241)'),
        legendrank=1,
        stackgroup='one'  # define stack group
    ))
    fig_actions.update_layout(
        template=graph_template,
        showlegend=True,
    )
    ################## ГРАФИК СДЕЛКИ ###########################
    actions_deals_df = actions_df.loc[actions_df['action_category'] == 'deal']

    number_of_deals_actions = actions_deals_df['count'].sum()
    deals_actions_graph_df = actions_deals_df.groupby(['created_at_date'], as_index=False).agg({'count': 'sum'})
    actions_x = deals_actions_graph_df['created_at_date']
    actions_deal_y = deals_actions_graph_df['count']

    fig_actions.add_trace(go.Scatter(
        x=actions_x,
        y=actions_deal_y,
        name='Сделки',
        # hoverinfo='x+y',
        mode='lines',
        # line=dict(width=0.5, color='rgb(131, 90, 241)'),
        legendrank=2,
        stackgroup='one'  # define stack group
    ))
    fig_actions.update_layout(
        template=graph_template,
        showlegend=True,
    )

    ################## ГРАФИК КАЛЕНДАРЬ ###########################
    actions_calendar_df = actions_df.loc[actions_df['action_category'] == 'calendar']
    number_of_calendar_actions = actions_calendar_df['count'].sum()
    calendar_actions_graph_df = actions_calendar_df.groupby(['created_at_date'], as_index=False).agg({'count': 'sum'})
    actions_x = calendar_actions_graph_df['created_at_date']
    actions_calendar_y = calendar_actions_graph_df['count']

    fig_actions.add_trace(go.Scatter(

        x=actions_x,
        y=actions_calendar_y,
        name='Календарь',
        # hoverinfo='x+y',
        mode='lines',
        legendrank=3,
        # line=dict(width=0.5, color='rgb(131, 90, 241)'),
        stackgroup='one'  # define stack group
    ))
    fig_actions.update_layout(
        template=graph_template,
        showlegend=True,
    )
    ################## ГРАФИК ПАРК ТЕХНИКИ ###########################
    actions_fleet_df = actions_df.loc[actions_df['action_category'] == 'fleet']
    number_of_fleet_actions = actions_fleet_df['count'].sum()
    fleet_actions_graph_df = actions_fleet_df.groupby(['created_at_date'], as_index=False).agg({'count': 'sum'})
    actions_x = fleet_actions_graph_df['created_at_date']
    actions_fleet_y = fleet_actions_graph_df['count']
    fig_actions.add_trace(go.Scatter(

        x=actions_x,
        y=actions_fleet_y,
        name='Парк техники',
        # hoverinfo='x+y',
        mode='lines',
        # line=dict(width=0.5, color='rgb(131, 90, 241)'),
        stackgroup='one'  # define stack group
    ))
    fig_actions.update_layout(
        template=graph_template,
        showlegend=True,
        # title_text='Действия пользователей, кол-во',
    )
    fig_actions.update_xaxes(
        showgrid=False,
        # ticklabelmode="period"
    )

    customer_actions_selector_options = checklist_customers_options_full_list
    deal_actions_selector_options = checklist_deals_options_full_list
    calendar_actions_selector_options = checklist_calendar_options_full_list
    fleet_actions_selector_options = checklist_fleet_options_full_list

    accordion_customers_title = 'КЛИЕНТЫ {}'.format(str(number_of_customers_actions))
    accordion_deals_title = 'СДЕЛКИ {}'.format(str(number_of_deals_actions))
    accordion_calendar_title = 'КАЛЕНДАРЬ {}'.format(str(number_of_calendar_actions))
    accordion_fleet_title = 'ПАРК ТЕХНИКИ {}'.format(str(number_of_fleet_actions))

    actions_table_html = actions_table.actions_table(actions_df)

    return customer_actions_selector_value, customer_actions_selector_options, deal_actions_selector_value, deal_actions_selector_options, calendar_actions_selector_value, calendar_actions_selector_options, fleet_actions_selector_value, fleet_actions_selector_options, accordion_customers_title, accordion_deals_title, accordion_calendar_title, accordion_fleet_title, fig_actions, actions_table_html


if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(host='0.0.0.0', debug=True)
