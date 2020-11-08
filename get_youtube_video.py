from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import json

def getVideo(titleName):
    load_dotenv(".env") # replace ".env" with whatever you named your file
    YT_API_KEY = os.environ.get('YT_API_KEY')
    api_key = YT_API_KEY

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(part="snippet", type="video", maxResults = 1, q = titleName)
    response = request.execute()

    videoId = response['items'][0]["id"]["videoId"]

    return videoId
