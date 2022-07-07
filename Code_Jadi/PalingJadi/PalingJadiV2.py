import requests

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()

input_negeri = 'johor'
input_zon    = 'mersing'
input_waktu  = 'zohor'

# def test():
for arkib in data['data']['negeri']:
    nama1 = arkib['nama']
    if input_negeri == nama1:
        for info in arkib['zon']:
            nama2 = info['nama']
            if input_zon == nama2:
                for maklumat in info['waktu_solat']:
                    nama3 = maklumat['name']
                    if input_waktu == nama3:
                        print(maklumat)
                    # else:
                    #     print(info['waktu_solat'])
                    # break
#         else:
#             print(arkib['zon'])
#             break
# else:
#     print(data['data']['negeri'])

                    # if input_negeri == nama1 and input_zon == nama2 and input_waktu == nama3:
                    #     print(maklumat)
                    #     break
                    # elif input_negeri == nama1 and input_zon == nama2:
                    #     print(info)
                    #     break
                    # elif input_negeri == nama1:
                    #     print(arkib)
                    #     break
