import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
import callbacks


radios_proj_tag = html.Div(
    [
        dbc.Label("项目类型", width=1),
            dbc.RadioItems(
                id="project-tag-radio",
                options=[
                    {"label": "产品开发", "value": 1},
                    {"label": "产品预研", "value": 2},
                    {"label": "技术预研", "value": 3},
                    {"label": "工程", "value": 4},

                ],
                inline=True
            ),
    ]
)

input_proj_num = html.Div(
    [
        dbc.Label("项目编号"),
        dbc.Input(placeholder="", type="text"),
        dbc.FormText("输入项目编号"),
    ]
)

input_proj_name = html.Div(
    [
        dbc.Label("项目名称"),
        dbc.Input(placeholder="", type="text"),
        dbc.FormText("输入项目名称"),
    ]
)

input_proj_info = html.Div(
    [
        dbc.Label("目标描述"),
        dbc.Textarea(size="lg", placeholder=""),
        dbc.FormText("从范围、时间、成本和用户满意等方面陈述项目目标"),
    ]
)



modal_confirm_create_proj = html.Div(
    [
        dbc.Button("创建", id="btn-create-proj", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("请确认")),
                dbc.ModalBody("请再次确认创建项目"),
                dbc.ModalFooter(
                    dbc.Button(
                        "确认", id="btn-confirm-create-proj", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal-confirm-create-proj",
            is_open=False,
            
        ),
    ]
)

def layout():
    return html.Div([
        radios_proj_tag, html.Br(), input_proj_num, html.Br(), input_proj_name, html.Br(), input_proj_info, html.Br(), modal_confirm_create_proj 
    ])



