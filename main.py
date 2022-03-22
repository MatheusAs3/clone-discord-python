from asyncio.windows_events import NULL
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc



# Componentes
from components.server_name import c_serverName
from components.server_list import c_serverList
from components.channel_info import c_channelInfo





# SL - Server List
# SN - Server Name
# CI - Channel Info
# CL - Channel List
# CD - Channel Data
# UL - User List
# UI - User Info


roboto = "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap"
material_icons = 'https://fonts.googleapis.com/icon?family=Material+Icons'



app = dash.Dash(__name__, external_stylesheets=[roboto,material_icons,dbc.themes.CYBORG])







def c_ChannelButton(channelName,selected):


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






def c_ChannelList():

  st_container = "cl-ctn"
  st_category = "cl-ct"
  st_icon = "cl-icon"


  st_title_span = "cl-title-span"



  content = html.Div([
    html.Div([
      html.Span("Canais de Texto", className=st_title_span),
      html.Span("add", className=f"material-icons {st_icon}")

    ], className=st_category ),

    c_ChannelButton('chat-livre',False),
    c_ChannelButton('trabalho',False),
    c_ChannelButton('lolzinho',False),
    c_ChannelButton('csgo',False),
    c_ChannelButton('valorant',False),


  ], className=st_container)


  return content






def c_UserInfo():

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




def c_UserRow(name,isBot=False):
  st_container = "ul-ur"
  st_avatar = f"ul-av {'bot' if isBot else ''}"


  user = html.Div([
    html.Div(className=st_avatar),
    html.Strong(name),
    html.Span("Bot") if isBot else None
  ], className=st_container)



  return user





def c_UserList():

  st_container = "ul-ctn"
  st_role = "ul-role"



  content = html.Div([

    html.Span("Disponivel - 1", className=st_role),
    c_UserRow("Matheus"),

    html.Span("Offline - 18", className=st_role),
    c_UserRow("Koishi", isBot=True),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),
    c_UserRow("Fulano"),


  ], className=st_container)


  return content



def c_ChannelData():

  st_container = "cd-ctn"

  st_messages = "cd-msg"

  st_icon_email = "cd-icon-email"

  st_input_wrapper = "cd-input-wrapper"
  st_input = "cd-input"



  content = html.Div([

    html.Div([

      c_ChannelMessage('Matheus', '01/12/2022', 'Bom Dia.'),
      c_ChannelMessage('Koishi', '01/12/2022', [html.Div([c_mention('@Matheus'), ", Brabo"])], isBot=True, hasMention=True),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_ChannelMessage('Fulano', '01/12/2022', 'bom dia'),




    ], className=st_messages),

    html.Div([
      dcc.Input(type="text",className=st_input,placeholder="Conversar #chat-livre"),
      html.Span("alternate_email", className=f"material-icons {st_icon_email}")
    ], className=st_input_wrapper)

  ], className=st_container)


  return content



def c_ChannelMessage(author,date,content, hasMention=False,isBot=False):
  st_container = f"cm-ctn {'mention' if hasMention else ''}"

  st_avatar = f"cm-avatar {'bot' if isBot else ''}"
  st_message = "cm-message"
  st_header = "cm-header"
  st_content = "cm-content"


  msg = html.Div([
    html.Div(className=st_avatar),

    html.Div([
      html.Div([
        html.Strong(author),
        html.Time(date),

        html.Span("Bot") if isBot else None,
        
      ], className=st_header),


      html.Div(content, className=st_content),
    ], className=st_message)


  ], className=st_container)


  return msg



def c_mention(name):

  cm_mention = "cm-mention"

  mention = html.Span(name, className=cm_mention)

  return mention












app.layout = html.Div([

  c_serverList(),
  c_serverName(),
  c_channelInfo(),
  c_ChannelList(),
  c_UserInfo(),
  c_ChannelData(),
  c_UserList(),


], className="grid-container")



















if __name__ == "__main__":
    app.run_server(debug=True, port=1051)