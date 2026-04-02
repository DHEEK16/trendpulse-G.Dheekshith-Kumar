!pip3 install requests  

import requests

url = "https://wttr.in/india"

response = requests.get(url, params = {"format": "j1"})
print(response)


response.json()

