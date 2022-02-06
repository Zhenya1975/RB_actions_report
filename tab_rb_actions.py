from dash import dcc, html
import dash_bootstrap_components as dbc


def tab_rb_actions():
    tab_rb_actions_content = dcc.Tab(
        label='Действия пользователей',
        value='user_actions_tab',
        # className='custom-tab',
        # selected_className='custom-tab--selected',
        children=[dbc.Row([
            dbc.Col(width=3,
                    children=[
                        html.Div(
                            children=[
                                html.Div(style={'marginLeft': '3px'},
                                         children=[
                                             html.P(),
                                             html.Div(id='plan_fact_tab_region_div_checklist',
                                                      children=[

                                                          html.P(),

                                                          dbc.Button("Выбрать все", size="sm",
                                                                     id="select_all_regions_button_tab_plan_fact",
                                                                     style={'marginBottom': '3px',
                                                                            'marginTop': '3px',
                                                                            'backgroundColor': '#232632'}
                                                                     ),
                                                          dbc.Button("Снять выбор", color="secondary",
                                                                     size="sm",
                                                                     style={'marginBottom': '3px',
                                                                            'marginTop': '3px',
                                                                            'backgroundColor': '#232632'},
                                                                     id="release_all_regions_button_tab_plan_fact"),

                                                          html.P(),
                                                          dcc.Checklist(
                                                              id='region_selector_checklist_tab_plan_fact',
                                                              # options=regions,
                                                              # value=regions_list,
                                                              labelStyle=dict(display='block')),
                                                          html.Hr(className="hr"),

                                                      ],
                                                      ),
                                             html.Div(
                                                 id='managers_check-list_div_tab_plan_fact',
                                                 children=[
                                                     # блок чек-боксов с Менеджерами
                                                     html.P(),
                                                     dbc.Button("Выбрать все", size="sm",
                                                                id="select_all_managers_button_tab_plan_fact",
                                                                style={'marginBottom': '3px',
                                                                       'marginTop': '3px',
                                                                       'backgroundColor': '#232632'}
                                                                ),
                                                     dbc.Button("Снять выбор", color="secondary",
                                                                size="sm",
                                                                style={'marginBottom': '3px',
                                                                       'marginTop': '3px',
                                                                       'backgroundColor': '#232632'},
                                                                id="release_all_managers_button_tab_plan_fact"),
                                                     html.P(),
                                                     dcc.Checklist(
                                                         id='managers_selector_checklist_tab_plan_fact',
                                                         # options=regions,
                                                         # value=regions_list,
                                                         labelStyle=dict(display='block')
                                                     ),
                                                 ]
                                             )
                                         ]
                                         ),

                            ])

                    ]
                    ),
            dbc.Col(width=9,
                    children=[
                        html.Div(dcc.Graph(id="rb_actions_graph", config={'displayModeBar': False}),
                                 className="m-4"),
                        html.P(),
                        html.Div([
                            dcc.Tabs(
                                id="tabs-meetings-tables",
                                style={
                                    # 'width': '50%',
                                    # 'font-size': '200%',
                                    # 'height':'5vh'
                                },
                                value='tab_plan_fact_managers',
                                # parent_className='custom-tabs',
                                # className='custom-tabs-container',
                                children=[
                                    dcc.Tab(
                                        label='Встречи. План-факт по менеджерам',
                                        value='tab_plan_fact_managers',
                                        # className='custom-tab',
                                        # selected_className='custom-tab--selected',
                                        children=[dbc.Row([
                                            dbc.Col(
                                                html.Div(id='users_plan_fact_table'),
                                            )])]),
                                    dcc.Tab(
                                        label='Клиенты. План-факт визитов',
                                        value='tab_plan_fact_customers',
                                        # className='custom-tab',
                                        # selected_className='custom-tab--selected',
                                        children=[dbc.Row([
                                            dbc.Col(children=[
                                                html.P(),
                                                html.Div(
                                                    dcc.Checklist(
                                                        id='customer_plan_fact_table_filter',
                                                        options=[{'label': ' План визитов выполнен  ', 'value': 1},
                                                                 {'label': ' План визитов не выполнен  ', 'value': 0},

                                                                 ],
                                                        value=[0, 1],
                                                        labelStyle=dict(display='inline')
                                                    ),
                                                ),

                                                html.P(),
                                                html.Div(id='customers_plan_fact_table'),
                                            ],

                                            )])]),

                                    # tab_calendar_actions.calendar_actions(),
                                    # tab_settings.tab_settings(),
                                    # tab2(),
                                    # tab3(),
                                ]
                            ),
                        ]),

                    ]),

        ]

        )]

    )
    return tab_rb_actions_content
