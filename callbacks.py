from flask_login import current_user
#from dash.exceptions import PreventUpdate

from app import app
from pages import project_page, create_page
from dash import Input, Output, State, callback, html
#from werkzeug.security import check_password_hash
from model import project, schedule, issue, timesheet, finance, submit, clear, display
from datetime import datetime, date, timedelta


@callback(
    Output("my-offcanvas", "is_open"),
    [Input("projects-link", "n_clicks")],
    [State("my-offcanvas", "is_open")],
)
def toggle_offcanvas(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("project-links", "children"),
    Input("my-offcanvas", "is_open")
)
def refresh_proj(open):
    if open:
        project_links = [
            html.Li(
                html.A(i.name, href=f"/project?id={i.number}")
            )
            for i in project.select()
        ]
        return project_links
    else:
        return None


@callback(
    Output('project-content', 'children'),
    [Input('url', 'pathname'), Input('url', 'search')],
    allow_duplicate=True
)
def display_project(pathname, search):
    if pathname == '/':
        return html.Div([
            html.H1("Tractor2"),
            html.P("Please click on the button to open the offcanvas."),
            html.Img(src="assets/logo.png", height="150px"),
        ])
    elif pathname == '/create':
        return create_page.layout()
    elif pathname == '/project':
        return project_page.layout(search)

    else:
        return "404 page Error"

        
# 在create页面点击提交数据时触发一个弹出窗口
@callback(
    Output("modal-confirm-create-proj", "is_open"),
    [Input("btn-create-proj", "n_clicks"), Input("btn-confirm-create-proj", "n_clicks")],
    [State("modal-confirm-create-proj", "is_open")],
    allow_duplicate=True,
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# 在create页面提交数据创建项目
@callback(
    Output("create-success-info", "is_open"),
    Input("btn-confirm-create-proj", "n_clicks"),
    [State("radio-project-tag", "value"),
    State("project-num", "value"),
    State("project-name", "value"),
    State("project-info", "value")]
)
def creat_project(n, tag, num, name, info):
    if n > 0:
        data = [{'tag': tag, 'number': num, 'name': name, 'info': info, 'updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]
        submit(project, data)
        return True