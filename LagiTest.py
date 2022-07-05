import requests


waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()

for info in data['data']:
    negeri = info['negeri']
    for zon in negeri['zon']:
        waktu_solat = zon['waktu_solat']
        for waktu in waktu_solat['name']:
            name = waktu_solat['name']
            time = waktu_solat['time']
            if name == 'subuh':
                print(f'waktu {name} adalah pada pukul {time}')