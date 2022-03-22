import dash
from dash import dcc, html


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







def c_serverList():
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