import requests

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()

input_negeri = 'wilayah persekutuan'
input_zon    = 'kuala lumpur'
input_waktu  = 'asar'

for arkib in data['data']['negeri']:
    nama1 = arkib['nama']
    daerah = arkib['zon']
    if input_negeri == nama1:
        for info in arkib['zon']:
            nama2 = info['nama']
            waktu_solat = info['waktu_solat']
            if input_zon == nama2:
                for maklumat in info['waktu_solat']:
                    nama3 = maklumat['name']
                    time = maklumat['time']
                    if input_waktu == nama3:
                        print(maklumat)
                        break
                else:
                    print(info['waktu_solat'])
                    break
        else:
            print(arkib['zon'])
            break
# else:
#     print(data['data']['negeri'])
