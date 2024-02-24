# <C> MoTechYT


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 20937822))
    API_HASH = os.environ.get("API_HASH", "68d3b463d3c53536782545f790aa5147")
    CAPTION = os.environ.get("CAPTION", "")
    BUTTON_TEXT = os.environ.get("BUTTON", "")
    URL_LINK = os.environ.get("LINK", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
