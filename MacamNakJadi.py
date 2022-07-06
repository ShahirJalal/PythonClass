from re import I
import requests

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()

# for info in data['data']:
#     for negeri in info['negeri']:
#         print(negeri)

# for key in data.keys():
#     if key == 'data':
#         # print(key)
#         for item in key['data']:
#             if item == 'negeri':
#                 print(item)

# negeri = 13
# zon = 2
# nama_waktu_solat = 6

input_negeri = 'wilayah persekutuan'
input_zon    = 'labuan'
input_waktu  = 'subuh'

# print(data['data']['negeri'][negeri]['zon'][zon]['waktu_solat'][waktu_solat])

for arkib in data['data']['negeri']:
    neme = arkib['nama']
    daerah = arkib['zon']
    if neme == input_negeri:
        for info in arkib['zon']:
            nama = info['nama']
            waktu_solat = info['waktu_solat']
            if nama == input_zon:
                for maklumat in info['waktu_solat']:
                    name = maklumat['name']
                    time = maklumat['time']
                    if name == input_waktu:
                        print(maklumat)

# for key in data.keys():
#     for item in data['data']:
#         print(data)

# for key in mydict.keys():
#     if key == 'cheese':
#         for item in mydict['cheese']:
#             if item == 'swiss':
#                 print(item)