from ast import And
import requests

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()

input_negeri = 'wilayah persekutuan'
input_zon    = 'kuala lumpur'
input_waktu  = 'subuh'

for arkib in data['data']['negeri']:
    nama1 = arkib['nama']
    daerah = arkib['zon']
    for info in arkib['zon']:
        nama2 = info['nama']
        waktu_solat = info['waktu_solat']
        for maklumat in info['waktu_solat']:
            nama3 = maklumat['name']
            time = maklumat['time']
            if input_negeri == nama1 and input_zon == nama2 and input_waktu == nama3:
                # print(arkib)
                # print(info)
                print(maklumat)
                break

            elif input_negeri == nama1 and input_zon == nama2 and input_waktu != nama3:
                print(info)
                break

            elif input_negeri == nama1 and input_zon != nama2 and input_waktu != nama3:
                print(arkib)
                break
    #                 else:
    #                     print('tak jadi waktu')
    #                     break
    #         else:
    #             print('tak jadi daerah')
    #             break
    # else:
    #     print('tak jadi negeri')
    #     break