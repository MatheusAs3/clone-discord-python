import dash
from dash import dcc, html
from dash.dependencies import Input, Output






def c_userRow(name,isBot=False):
  st_container = "ul-ur"
  st_avatar = f"ul-av {'bot' if isBot else ''}"


  user = html.Div([
    html.Div(className=st_avatar),
    html.Strong(name),
    html.Span("Bot") if isBot else None
  ], className=st_container)



  return user



def c_userList():

  st_container = "ul-ctn"
  st_role = "ul-role"



  content = html.Div([

    html.Span("Disponivel - 1", className=st_role),
    c_userRow("Matheus"),

    html.Span("Offline - 18", className=st_role),
    c_userRow("Koishi", isBot=True),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),
    c_userRow("Fulano"),


  ], className=st_container)


  return content