from flask import Flask, redirect, url_for
from dash import Dash, dcc, html
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from redis_connection import connect_to_redis, load_csv_to_redis
from redis_service import RedisService

app = Flask(__name__)
dash_app = Dash(__name__, server=app, url_base_pathname='/dashboard/')


redis_client = connect_to_redis()
load_csv_to_redis("focos_incendio.csv", redis_client)
redis_service = RedisService(redis_client)


dash_app.layout = html.Div([
    html.H1("Dashboard de Focos de Incêndio"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Focos por Estado', 'value': 'estado'},
            {'label': 'Focos por Município', 'value': 'municipio'},
            {'label': 'Risco Médio de Fogo por Estado', 'value': 'risco_estado'},
            {'label': 'Precipitação Média por Bioma', 'value': 'prec_bioma'},
            {'label': 'Focos por Mês', 'value': 'mes'}
        ],
        value='estado'
    ),
    dcc.Graph(id='graph')
])


@dash_app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_option):
    if selected_option == 'estado':
        data = redis_service.get_focos_por_estado()
        figure = {
            'data': [{'x': data.index, 'y': data.values, 'type': 'bar'}],
            'layout': {'title': 'Focos por Estado'}
        }
    elif selected_option == 'municipio':
        data = redis_service.get_focos_por_municipio()
        figure = {
            'data': [{'x': data.index, 'y': data.values, 'type': 'bar'}],
            'layout': {'title': 'Focos por Município'}
        }
    elif selected_option == 'risco_estado':
        data = redis_service.get_risco_fogo_medio_por_estado()
        figure = {
            'data': [{'x': data.index, 'y': data.values, 'type': 'bar'}],
            'layout': {'title': 'Risco Médio de Fogo por Estado'}
        }
    elif selected_option == 'prec_bioma':
        data = redis_service.get_precipitacao_media_por_bioma()
        figure = {
            'data': [{'x': data.index, 'y': data.values, 'type': 'bar'}],
            'layout': {'title': 'Precipitação Média por Bioma'}
        }
    elif selected_option == 'mes':
        data = redis_service.get_focos_por_mes()
        figure = {
            'data': [{'x': data.index.astype(str), 'y': data.values, 'type': 'line'}],
            'layout': {'title': 'Focos por Mês'}
        }
    return figure

@app.route('/')
def home():
    return redirect(url_for('/dashboard/'))  


if __name__ == '__main__':
    app.run(debug=True, port=8050)
