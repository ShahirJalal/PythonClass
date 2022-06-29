from cgitb import reset
from time import time
from urllib import response
import requests

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/states.json"

response = requests.get(waktu_solat_api)
data = response.json()

for maklumat in (data['data']['negeri'][0]['zon'][0]['waktu_solat']):
    print(time)