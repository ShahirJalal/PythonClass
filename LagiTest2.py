import requests


waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()

# for info in data['data']:
#     for negeri in info['negeri']:
#         print(negeri)

for key in data.keys():
    for item in data['data']:
        for item in data[0]:
            print(item)

# for key in data.keys():
#     for item in data['data']:
#         print(data)

# for key in mydict.keys():
#     if key == 'cheese':
#         for item in mydict['cheese']:
#             if item == 'swiss':
#                 print(item)