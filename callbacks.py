from flask_login import current_user
#from dash.exceptions import PreventUpdate

from app import app
from pages import project, create
from dash import Input, Output, State, callback, html
#from werkzeug.security import check_password_hash
import callbacks




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
        return create.layout()
    elif pathname == '/project':
        return project.layout(search)

    else:
        return "404 page Error"

        
# 在create页面点击创建时触发一个弹出窗口
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