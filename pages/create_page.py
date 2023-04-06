import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
import callbacks
from model import schedule, issue, timesheet, finance, submit, clear, display


radios_proj_tag = html.Div(
    [
        dbc.Label("项目类型", width=1),
            dbc.RadioItems(
                id="radio-project-tag",
                options=[
                    {"label": "产品开发", "value": "产品开发"},
                    {"label": "产品预研", "value": "产品预研"},
                    {"label": "技术预研", "value": "技术预研"},
                    {"label": "工程", "value": "工程"},

                ],
                inline=True
            ),
    ]
)

input_proj_num = html.Div(
    [
        dbc.Label("项目编号"),
        dbc.Input(placeholder="", type="text", id="project-num",),
    ]
)

input_proj_name = html.Div(
    [
        dbc.Label("项目名称"),
        dbc.Input(placeholder="", type="text", id="project-name"),
    ]
)

input_proj_info = html.Div(
    [
        dbc.Label("目标描述"),
        dbc.Textarea(placeholder="从范围、时间、成本和用户满意等方面陈述项目目标", id="project-info"),
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

create_success_info = dbc.Alert("创建项目成功！", id='create-success-info', dismissable=True, duration=5000, is_open=False)

def layout():
    return html.Div([
        radios_proj_tag, html.Br(), input_proj_num, html.Br(), input_proj_name, html.Br(), input_proj_info, html.Br(), modal_confirm_create_proj, create_success_info 
    ])



