import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State

def layout(search):
    id_value = search.split('=')[-1]
    return html.Div([
            html.H1(f"项目名称: {id_value}"),
            dbc.Tabs([
            dbc.Tab(label="日程", children=[
                html.P("This is the content of 日程."),
            ], tab_id="tab-1"),
            dbc.Tab(label="问题", children=[
                html.P("This is the content of 问题."),
            ], tab_id="tab-2"),
            dbc.Tab(label="财务", children=[
                html.P("This is the content of 财务."),
            ], tab_id="tab-3"),
            dbc.Tab(label="文档", children=[
                html.P("This is the content of 文档."),
            ], tab_id="tab-4"),
            dbc.Tab(label="需求", children=[
                html.P("This is the content of 需求."),
            ], tab_id="tab-5"),
            dbc.Tab(label="成员", children=[
                html.P("This is the content of 成员."),
            ], tab_id="tab-6"),            
            dbc.Tab(label="工时", children=[
                html.P("This is the content of 工时."),
            ], tab_id="tab-7"),
        ],
        id="tabs",
        active_tab="tab-1",
        )
    ])