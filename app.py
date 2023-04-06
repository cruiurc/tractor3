import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from pages import create_page, project_page
import callbacks
from model import project


project_links = [
    html.Li(
        html.A(project.name, href=f"/project?id={project.number}")
    )
    for project in project.select()
]


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/logo.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Tractor2", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavItem(dbc.NavLink("新建", href="/create"), style={"color": "white"})),
                        dbc.Col(dbc.NavItem(dbc.NavLink("整合", href="#"), style={"color": "white"})),
                        dbc.Col(dbc.NavItem(dbc.NavLink("项目", href="/project", id="projects-link"), style={"color": "white"}))
                    ],
                    align="center",
                    className="row row-cols-auto",                    
                ),
            )
        ]
    ),
    color="dark",
    dark=True,
)


offcanvas = dbc.Offcanvas(
    children=[
        html.Ul(
            project_links,
            className="nav flex-column",
        ),
    ],
    id="my-offcanvas",
    title="My Offcanvas",
    placement="end"
    
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    offcanvas,
    html.Div([html.A("There's nothing here yet")],
             id='project-content',
             ),
])

app.config.suppress_callback_exceptions = True


server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)

