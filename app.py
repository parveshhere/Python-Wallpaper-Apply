import ctypes
import requests
import urllib.request
import json
import random

def displayImageAsWallpaper(AbsoluteImagePath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 0)


apikey = "yourapikey"
url=f'https://api.unsplash.com/photos/?client_id={apikey}'
x = requests.get(url)

response = json.loads(x.text)

random_no = random.randint(0, 9)


image = response[random_no]['urls']['full']
PATH = urllib.request.urlretrieve(image)[0]
displayImageAsWallpaper(PATH)
