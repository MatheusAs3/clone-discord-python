import dash
from dash import dcc, html
from dash.dependencies import Input, Output


from components.channel_button import c_channelButton



def c_channelList():

  st_container = "cl-ctn"
  st_category = "cl-ct"
  st_icon = "cl-icon"


  st_title_span = "cl-title-span"



  content = html.Div([
    html.Div([
      html.Span("Canais de Texto", className=st_title_span),
      html.Span("add", className=f"material-icons {st_icon}")

    ], className=st_category ),

    c_channelButton('chat-livre',False),
    c_channelButton('trabalho',False),
    c_channelButton('lolzinho',False),
    c_channelButton('csgo',False),
    c_channelButton('valorant',False),


  ], className=st_container)


  return content