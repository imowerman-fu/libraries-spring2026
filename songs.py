import json
import requests
import sys

response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + sys.argv[2] + "&term=" + sys.argv[1]   ) 

o = response.json()

for result in o["results"]:
    print(result["trackName"]) 