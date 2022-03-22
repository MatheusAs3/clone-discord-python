from asyncio.windows_events import NULL
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


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


class ServerButton():
  def __init__(self,selectd,isHome,hasNotifications,mentions):
    self.selectd = selectd
    self.isHome = isHome
    self.hasNotifications = hasNotifications
    self.mentions = mentions

  
  def get(self):

    extra_class = ""

    if self.hasNotifications:
      extra_class += " not"

    if self.isHome:
      serverButton = html.Button(html.Img(src="https://svgshare.com/i/Pb9.svg", alt="Discord", className="sl-img"), className=f"sl-bt-home{extra_class}")

      if self.mentions > 0:
        extra_class += " men"
        serverButton = html.Button(html.Img(src="https://svgshare.com/i/Pb9.svg", alt="Discord", className="sl-img"), className=f"sl-bt-home{extra_class}", value=str(self.mentions))

    else:
      serverButton = html.Button(className=f"sl-bt{extra_class}")   

      if self.mentions > 0:
        extra_class += " men"
        serverButton = html.Button(className=f"sl-bt{extra_class}", value=str(self.mentions))  



    return serverButton







def c_ServerList():
  st_container = "sl-ctn"
  st_separator = "sl-sp"


  content = html.Div([

    ServerButton(False,True,False,0).get(),
    html.Div(className=st_separator),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,True,0).get(),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,False,4).get(),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,False,73).get(),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,False,0).get(),
    ServerButton(False,False,True,333).get(),

  ], className=st_container)


  return content



def c_ServerName():

  st_container = "sn-ctn"
  st_title = "sn-title"
  st_icon = "sn-icon"


  content = html.Div([

    html.H1("Servidor de Teste", className=st_title),
    html.Span("expand_more", className=f"material-icons {st_icon}")


  ], className=st_container)


  return content




def c_ChannelInfo():
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

  c_ServerList(),
  c_ServerName(),
  c_ChannelInfo(),
  c_ChannelList(),
  c_UserInfo(),
  c_ChannelData(),
  c_UserList(),


], className="grid-container")



















if __name__ == "__main__":
    app.run_server(debug=True, port=1051)