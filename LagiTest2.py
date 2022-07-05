import request

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = request.get(waktu_solat_api)
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

print(data['data']['negeri'][0]['zon'][0]['waktu_solat']['name','time'])

# for key in data.keys():
#     for item in data['data']:
#         print(data)

# for key in mydict.keys():
#     if key == 'cheese':
#         for item in mydict['cheese']:
#             if item == 'swiss':
#                 print(item)