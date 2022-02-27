from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import initial_values
import datetime
loading_style = {
    # 'position': 'absolute',
    # 'align-self': 'center'
                 }

def tab_settings():
    tab_settings_block = dcc.Tab(
        label='Настройки',
        value='tab_settings',
        # className='custom-tab',
        # selected_className='custom-tab--selected',
        children=[dbc.Row([
            html.Div(
                children=[
                    dcc.Loading(id='loading', parent_style=loading_style),
                    dbc.Alert(

                        id="alert-success",
                        # dismissable=True,
                        color="success",
                        # is_open=False,
                        duration=4000,

                        style={"marginLeft": 5, "marginRight": 5, "marginTop": 5}

                    ),
                    dbc.Alert(

                        id="alert-danger",
                        # dismissable=True,
                        # is_open=False,
                        duration=4000,
                        color="danger",
                        style={"marginLeft": 5, "marginRight": 5, "marginTop": 5}

                    ),
                ],


            ),

            dbc.Col(
                # width=3,
                children=[

                    # html.Div(id='alert_upload'), html.P('В отчет План-факт встреч включить:'), dcc.RadioItems( id =
                    # 'meetings_data_selector', options=[ {'label': ' Все завершенные встречи',
                    # 'value': 'include_all_meetings'}, {'label': ' Только встречи, идущие в зачет погашения нормы
                    # визитов', 'value': 'include_plan_fact_meetings'}, ], value='include_all_meetings',
                    # labelStyle=dict(display='block'), ), html.Hr(),
                    html.P(),
                    dbc.Label(id="csv_url_label"),
                    dbc.Input(id="input_csv_url", type="text"),
                    html.P(),
                    html.P("Период отчета"),
                    # ряд, в котором лежат дроплисты с годом и кварталом
                    dbc.Row([
                        dbc.Col(width=3,
                                children=[
                                    html.Div(style={'paddingLeft': '5px', 'paddingRight': '5px', },
                                             children=[
                                                 html.Div(id='test', children=[html.P()]),
                                                 dcc.Dropdown(
                                                     id='quarter_selector',
                                                     options=[
                                                         {'label': '1-й кв',
                                                          'value': 1},
                                                         {'label': '2-й кв',
                                                          'value': 2},
                                                         {'label': '3-й кв',
                                                          'value': 3},
                                                         {'label': '4-й кв',
                                                          'value': 4},
                                                     ],
                                                     placeholder='Квартал',
                                                     clearable=False,
                                                     # value=initial_values.get_current_quarter_and_year()[0],
                                                     value=3
                                                 ),
                                             ]),
                                    html.Div(style={'paddingLeft': '5px',
                                                    'paddingRight': '5px',
                                                    'paddingTop': '3px', },
                                             children=[
                                                 dcc.Dropdown(
                                                     id='year_selector',
                                                     options=[

                                                         {'label': '2020',
                                                          'value': 2020},
                                                         {'label': '2021',
                                                          'value': 2021},
                                                         {'label': '2022',
                                                          'value': 2022},
                                                     ],
                                                     placeholder='Год',
                                                     clearable=False,
                                                     # value=initial_values.get_current_quarter_and_year()[1]
                                                     value=2021
                                                 ),
                                             ]),

                                ]
                                ),

                    ]
                    ),
                    html.P(id='update_daterange'),
                    # html.Div([
                    #     dcc.DatePickerRange(
                    #         id='dataset-date-picker-range',
                    #         first_day_of_week=1,
                    #         # min_date_allowed=date(1995, 8, 5),
                    #         # max_date_allowed=datetime.datetime.now().date(),
                    #         initial_visible_month=datetime.datetime.now().date(),
                    #         # start_date = datetime.datetime.now().date(),
                    #         start_date=datetime.datetime.strptime("01.11.2021", "%d.%m.%Y").date(),
                    #         # end_date=datetime.datetime.now().date(),
                    #         end_date=datetime.datetime.strptime("31.12.2021", "%d.%m.%Y").date(),
                    #         display_format='D.M.YYYY',
                    #     ), ]),
                    # html.A(dbc.Button("Обновить", size="sm",
                    #                   style={'marginBottom': '3px',
                    #                          'marginTop': '3px',
                    #                          'backgroundColor': '#232632'}
                    #                   ), href='/'),
                    dbc.Button("Обновить", size="sm",
                               style={'marginBottom': '3px',
                                      'marginTop': '3px',
                                      'backgroundColor': '#232632'},
                               id="update_dataset_btn"

                               )

                    # dcc.Upload(dbc.Button("Загрузить файл", color="secondary",
                    #                       size="md",
                    #                       style={'marginBottom': '3px',
                    #                              'marginTop': '3px',
                    #                              'backgroundColor': '#232632'},
                    #                       ),
                    #            id="upload_meetings"
                    #            ),
                    # html.Div([
                    #     html.A("Выгрузить Excel шаблон встреч",
                    #            style={'color': 'blue',
                    #                   # 'textDecoration': 'none'
                    #                   },
                    #            id="btn_xlsx"),
                    #     dcc.Download(id="download-meetings-xlsx"),
                    # ]),

                ]

            )
        ]

        )]

    )
    return tab_settings_block
