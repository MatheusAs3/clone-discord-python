import dash
from dash import dcc, html
from dash.dependencies import Input, Output






def c_userInfo():

  st_container = "ui-ctn"
  st_profile = "ui-profile"
  st_avatar = "ui-avatar"
  st_user_data = "ui-user-data"
  

  


  st_icons = "ui-icons"
  st_icon_mic = "ui-icon-mic"
  st_icon_headset = "ui-icon-headset"
  st_icon_settings = "ui-icon-settings"



  content = html.Div([

    html.Div([

      html.Div([


      ], className=st_avatar),


      html.Div([
        html.Strong("Matheus"),
        html.Span("#3333")
      ], className=st_user_data),

    ], className=st_profile),




    html.Div([
      html.Span("mic", className=f"material-icons {st_icon_mic}"),
      html.Span("headset", className=f"material-icons {st_icon_headset}"),
      html.Span("settings", className=f"material-icons {st_icon_settings}"),
    ], className= st_icons),



  ], className=st_container)


  return content