import dash
from dash import dcc, html


def c_serverName():

  st_container = "sn-ctn"
  st_title = "sn-title"
  st_icon = "sn-icon"


  content = html.Div([

    html.H1("Servidor de Teste", className=st_title),
    html.Span("expand_more", className=f"material-icons {st_icon}")


  ], className=st_container)


  return content



