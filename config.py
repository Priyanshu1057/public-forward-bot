import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23685822"))
    API_HASH = os.environ.get("API_HASH", "ff0572e13ff2f63a50f6dc707e0c4c9f")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6725874739")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://priyanshu1234:<d8Nau3FLAe4WwYGm>@cluster0.w7grbtg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002791703512"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Trial_filestorep1bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
