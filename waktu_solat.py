import requests
import sys

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"

response = requests.get(waktu_solat_api)
data = response.json()

for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
    print(maklumat['time'])

def grab_api():
    waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
    response = requests.get(waktu_solat_api)
    data = response.json()
    return data

def filter_results():
    for info in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
        nama = info['name']
        waktu = info['time']
        if info['name'] == waktu_solat_api:
            print(f'Waktu {nama} adalah pada: {waktu}')

def get_input(nama, waktu):
    nama = sys.argv[1]
    waktu = sys.argv[2]

# Siapkan