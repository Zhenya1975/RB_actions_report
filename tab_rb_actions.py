from dash import dcc, html
import dash_bootstrap_components as dbc
import datetime


def tab_rb_actions():
    tab_rb_actions_content = dcc.Tab(
        label='Действия пользователей',
        value='user_actions_tab',
        # className='custom-tab',
        # selected_className='custom-tab--selected',
        children=[dbc.Row([
            html.P(),
            dbc.Col(width=3,
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    dbc.Accordion(
                                        [
                                            dbc.AccordionItem(
                                                [
                                                    html.Div(id='customers_div_checklist',
                                                             children=[

                                                                 # html.H4('КЛИЕНТЫ'),
                                                                 dbc.Button("Выбрать все", size="sm",
                                                                            id="select_all_customer_actions",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'}
                                                                            ),
                                                                 dbc.Button("Снять выбор", color="secondary",
                                                                            size="sm",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'},
                                                                            id="release_all_customer_actions"),

                                                                 html.P(),
                                                                 dcc.Checklist(
                                                                     id='customer_actions_selector',
                                                                     # options=regions,
                                                                     # value=
                                                                     labelStyle=dict(display='block')),
                                                                 html.Hr(className="hr"),

                                                             ],
                                                             ),
                                                ],

                                                # title='КЛИЕНТЫ {}'.format(12),
                                                title='КЛИЕНТЫ',
                                                id="accordion_customers"
                                            ),
                                            dbc.AccordionItem(
                                                [
                                                    html.Div(id='deals_div_checklist',
                                                             children=[

                                                                 # html.H4('СДЕЛКИ'),
                                                                 dbc.Button("Выбрать все", size="sm",
                                                                            id="select_all_deal_actions",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'}
                                                                            ),
                                                                 dbc.Button("Снять выбор", color="secondary",
                                                                            size="sm",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'},
                                                                            id="release_all_deal_actions"),

                                                                 html.P(),
                                                                 dcc.Checklist(
                                                                     id='deal_actions_selector',
                                                                     # options=regions,
                                                                     # value=
                                                                     labelStyle=dict(display='block')),
                                                                 html.Hr(className="hr"),

                                                             ],
                                                             ),
                                                ],
                                                # title="СДЕЛКИ",
                                                id="accordion_deals"
                                            ),

                                            dbc.AccordionItem(
                                                [
                                                    html.Div(id='calendar_div_checklist',
                                                             children=[


                                                                 dbc.Button("Выбрать все", size="sm",
                                                                            id="select_all_calendar_actions",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'}
                                                                            ),
                                                                 dbc.Button("Снять выбор", color="secondary",
                                                                            size="sm",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'},
                                                                            id="release_all_calendar_actions"),

                                                                 html.P(),
                                                                 dcc.Checklist(
                                                                     id='calendar_actions_selector',
                                                                     # options=regions,
                                                                     # value=
                                                                     labelStyle=dict(display='block')),
                                                                 html.Hr(className="hr"),

                                                             ],
                                                             ),
                                                ],
                                                # title="СДЕЛКИ",
                                                id="accordion_calendar"
                                            ),
                                            dbc.AccordionItem(
                                                [
                                                    html.Div(id='fleet_div_checklist',
                                                             children=[

                                                                 dbc.Button("Выбрать все", size="sm",
                                                                            id="select_all_fleet_actions",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'}
                                                                            ),
                                                                 dbc.Button("Снять выбор", color="secondary",
                                                                            size="sm",
                                                                            style={'marginBottom': '3px',
                                                                                   'marginTop': '3px',
                                                                                   'backgroundColor': '#232632'},
                                                                            id="release_all_fleet_actions"),

                                                                 html.P(),
                                                                 dcc.Checklist(
                                                                     id='fleet_actions_selector',
                                                                     # options=regions,
                                                                     # value=
                                                                     labelStyle=dict(display='block')),
                                                                 html.Hr(className="hr"),

                                                             ],
                                                             ),
                                                ],
                                                # title="ПАРК ТЕХНИКИ",
                                                id="accordion_fleet"
                                            ),
                                        ],
                                        start_collapsed=True,
                                    )
                                ),
                                html.Div(style={'marginLeft': '3px'},
                                         children=[
                                             html.P(),



                                         ]
                                         ),

                            ])

                    ]
                    ),
            dbc.Col(width=9,
                    children=[
                        html.Div([
                            dcc.DatePickerRange(
                                id='my-date-picker-range',
                                first_day_of_week=1,
                                # min_date_allowed=date(1995, 8, 5),
                                # max_date_allowed=datetime.datetime.now().date(),
                                initial_visible_month=datetime.datetime.now().date(),
                                # start_date = datetime.datetime.now().date(),
                                # start_date=datetime.datetime.strptime("01.11.2021", "%d.%m.%Y").date(),
                                # end_date=datetime.datetime.now().date(),
                                # end_date=datetime.datetime.strptime("31.12.2021", "%d.%m.%Y").date(),
                                display_format='DD.MM.YYYY',
                            ), ]),
                        html.Div(dcc.Graph(id="rb_actions_graph", config={'displayModeBar': False}),
                                 className="m-4"),
                        html.P(),
                        html.P(),
                        html.Div(id='user_actions_table'),
                        # html.Div([
                        #     dcc.Tabs(
                        #         id="tabs-meetings-tables",
                        #         style={
                        #             # 'width': '50%',
                        #             # 'font-size': '200%',
                        #             # 'height':'5vh'
                        #         },
                        #         value='tab_plan_fact_managers',
                        #         # parent_className='custom-tabs',
                        #         # className='custom-tabs-container',
                        #         children=[
                        #             dcc.Tab(
                        #                 label='Встречи. План-факт по менеджерам',
                        #                 value='tab_plan_fact_managers',
                        #                 # className='custom-tab',
                        #                 # selected_className='custom-tab--selected',
                        #                 children=[dbc.Row([
                        #                     dbc.Col(
                        #                         html.Div(id='users_plan_fact_table'),
                        #                     )])]),
                        #             dcc.Tab(
                        #                 label='Клиенты. План-факт визитов',
                        #                 value='tab_plan_fact_customers',
                        #                 # className='custom-tab',
                        #                 # selected_className='custom-tab--selected',
                        #                 children=[dbc.Row([
                        #                     dbc.Col(children=[
                        #                         html.P(),
                        #                         html.Div(
                        #                             dcc.Checklist(
                        #                                 id='customer_plan_fact_table_filter',
                        #                                 options=[{'label': ' План визитов выполнен  ', 'value': 1},
                        #                                          {'label': ' План визитов не выполнен  ', 'value': 0},
                        #
                        #                                          ],
                        #                                 value=[0, 1],
                        #                                 labelStyle=dict(display='inline')
                        #                             ),
                        #                         ),
                        #
                        #                         html.P(),
                        #                         html.Div(id='customers_plan_fact_table'),
                        #                     ],
                        #
                        #                     )])]),
                        #
                        #             # tab_calendar_actions.calendar_actions(),
                        #             # tab_settings.tab_settings(),
                        #             # tab2(),
                        #             # tab3(),
                        #         ]
                        #     ),
                        # ]),

                    ]),

        ]

        )]

    )
    return tab_rb_actions_content
