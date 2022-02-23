import plotly.graph_objects as go
import pandas as pd
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc

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
    "sandstone"
]
available_graph_templates: ['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark',
                            'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']
load_figure_template(templates)

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)


############# PIECHART ACTIONS ПО КАТЕГОРИЯМ #####################
def fig_piechart_actions_by_categories(actions_df, theme_selector):
    actions_categ = actions_df.groupby('Категория', as_index=False).size()

    labels = list(actions_categ['Категория'])
    values = list(actions_categ['size'])
    if theme_selector:
        graph_template = 'seaborn'
    else:
        graph_template = 'plotly_dark'
    action_piechart = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # planned_downtime_piechart.update_traces(textposition='inside')
    action_piechart.update_layout(
        # margin=dict(t=0, b=0, l=0, r=0),
        autosize=False,
        width=400,
        height=400,
        title_text='Действия по категориям',
        template=graph_template,
        # uniformtext_minsize=12, uniformtext_mode='hide',
        legend=dict(
            # font=dict(color='#7f7f7f'),
            orientation="h", # Looks much better horizontal than vertical
            # y=0.6,
            # x=1.6
        ),
    )
    return action_piechart