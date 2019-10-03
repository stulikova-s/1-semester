from pprint import pprint
import requests
from urllib.parse import urljoin
from pathlib import Path
import os

api_token = '###'
username = '###'
pythonanywhere_host = "www.pythonanywhere.com"

api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
    pythonanywhere_host=pythonanywhere_host,
    username=username,
)

for root, dirs, files in os.walk("./Work"):
    for filename in files:
    	resp = requests.post(urljoin(api_base, 'files/path/home/{username}/steph/templates/zim/{item}'.format(username=username,item=root[2:]+'/'+filename)),
    		files={"content":open('{item}'.format(item=root[2:]+'/'+filename))},
    		headers={"Authorization": "Token {api_token}".format(api_token=api_token)})
