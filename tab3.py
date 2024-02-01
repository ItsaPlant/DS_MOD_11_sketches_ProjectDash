import dash
from dash import html, dcc
import plotly.graph_objects as go
import html2dash

def render_tab(df):

    layout = html.Div([html.H1('Pipelines',style={'text-align':'center'}),
                        html.Div([dcc.DatePickerRange(id='sales-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='bar-pipe')],style={'width':'50%'}),
                        html.Div([dcc.Graph(id='choropleth-pipe')],style={'width':'50%'})],style={'display':'flex'})
                        ])

    return layout