import requests
import base64

client_id = "a"
client_secret = "b"

a = client_id+':'+client_secret
# b = str(base64.b64decode(a))
print()

url = 'https://accounts.spotify.com/api/token'

auth_options = {
    "headers": {
        # 'Authorization': 'Basic ' + b,
        'Content-Type': 'application/x-www-form-urlencoded'
    },

    "grant_type": 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

x = requests.post('https://accounts.spotify.com/api/token', auth_options)
print(x.text)

