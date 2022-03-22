import dash
from dash import dcc, html
from dash.dependencies import Input, Output


def c_channelButton(channelName,selected):


  st_container = "cb-ctn"
  
  st_icon_h = "cb-icon-hashtag"

  st_icon_add = "cb-icon-add"
  st_icon_settings = "cb-icon-settings"


  content = html.Div([



    html.Div([
      html.Img(src="/assets/icons/hashtag.svg", className=st_icon_h),
      html.Span(channelName, className="cb-cn")

    ], className= 'active' if selected else '' ),




    html.Div([
      html.Span("person_add", className=f"material-icons {st_icon_add}"),
      html.Span("settings", className=f"material-icons {st_icon_settings}"),
    ], className = "settings"),



  ], className=st_container)


  return content