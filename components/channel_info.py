import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def c_channelInfo():
  st_container = "ci-ctn"
  st_icon = "ci-icon"
  st_title = "ci-title"
  st_separator = "ci-sp"
  st_discription = "ci-dp"


  content = html.Div([

    html.Img(src="/assets/icons/hashtag.svg", className=st_icon),
    html.H1("chat-livre", className=st_title),
    html.Div(className=st_separator),
    html.Span("Canal aberto para conversas", className=st_discription)


  ], className=st_container)


  return content