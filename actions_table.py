from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc


def actions_table(actions_df):
    actions_df = actions_df.loc[:, ['created_at_date', 'Категория', 'action']]
    actions_df["created_at_date"] = actions_df["created_at_date"].astype("datetime64[ns]")
    actions_df["created_at_date"] = actions_df["created_at_date"].dt.strftime("%d.%m.%Y")

    actions_df.rename(columns={'created_at_date': 'Дата', 'description': 'Описание', 'action': 'Действие'},
                      inplace=True)

    action_table_html = html.Div(
        [
            dash_table.DataTable(

                data=actions_df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in actions_df.columns],
                # filter_action='native',
                style_header={
                    # 'backgroundColor': 'white',
                    'fontWeight': 'bold'
                },
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
                style_cell={'textAlign': 'left'},

            ),

            html.Hr(),  # horizontal line

            # For debugging, display the raw contents provided by the web browser
            # html.Div('Raw Content'),
            # html.Pre(contents[0:200] + '...', style={
            #     'whiteSpace': 'pre-wrap',
            #     'wordBreak': 'break-all'
            # })
        ], style={'margin-right': 50})
    return action_table_html
