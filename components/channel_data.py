import dash
from dash import dcc, html
from dash.dependencies import Input, Output










def c_channelData():

  st_container = "cd-ctn"

  st_messages = "cd-msg"

  st_icon_email = "cd-icon-email"

  st_input_wrapper = "cd-input-wrapper"
  st_input = "cd-input"



  content = html.Div([

    html.Div([

      c_channelMessage('Matheus', '01/12/2022', 'Bom Dia.'),
      c_channelMessage('Koishi', '01/12/2022', [html.Div([c_mention('@Matheus'), ", Brabo"])], isBot=True, hasMention=True),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),
      c_channelMessage('Fulano', '01/12/2022', 'bom dia'),




    ], className=st_messages),

    html.Div([
      dcc.Input(type="text",className=st_input,placeholder="Conversar #chat-livre"),
      html.Span("alternate_email", className=f"material-icons {st_icon_email}")
    ], className=st_input_wrapper)

  ], className=st_container)


  return content



def c_channelMessage(author,date,content, hasMention=False,isBot=False):
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




