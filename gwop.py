#GUWOP BOT
#t4C41XOLaUW60TxrdSPZDQzA8iVd03vMwyZAC2zs

#TODO
#
#
#
#
import json, requests

test_bot_id  = '39b89f4af5caf7409d2b3e34db'
guwop_bot_id = '187e66ee287e48feb4db037d87'

def getPeterID():
    None

def likePeterMessage():
    None

def sendMessage(text):
    requests.post("https://api.groupme.com/v3/bots/post", None,{  "bot_id"  : "39b89f4af5caf7409d2b3e34db",
  "text": text})


if __name__ == '__main__':
    sendMessage("suhhh")
