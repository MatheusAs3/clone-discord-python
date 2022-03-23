from asyncio.windows_events import NULL
import re
from tkinter import N
import dash
from dash import dcc, html, callback_context

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Componentes
from components.server_name import c_serverName
from components.server_list import c_serverList
from components.channel_info import c_channelInfo
from components.channel_list import c_channelList
from components.user_info import c_userInfo
from components.user_list import c_userList
from components.channel_data import c_channelData

from components.channel_data import c_channelMessage




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








layour_server = html.Div([

  c_serverList(),
  c_serverName(),
  c_channelInfo(),
  c_channelList(),
  c_userInfo(),
  c_channelData(),
  c_userList(),


], className="grid-container")








app.layout = layour_server



@app.callback([Output("Data1", "children"), Output("Chat1", "value")],
[
  Input("Chat1", "value"),
  Input("Data1", "children"),
  Input("Chat1", "n_submit"),

])
def show_chat(text,data,n_submit):
  texto = text
  data = data
  new = None
 
  changed_id = [p['prop_id'] for p in callback_context.triggered][0]

  print(changed_id)

  if 'Chat1.n_submit' in changed_id:
    new = c_channelMessage('Matheus', '01/12/2022', texto)
    data.append(new)
    texto = ""
    return (data, texto)

  
  

  return (data, texto)



  
 
  

  





if __name__ == "__main__":
    app.run_server(debug=True, port=1051)