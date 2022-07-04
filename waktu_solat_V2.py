import requests
import sys

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"

response = requests.get(waktu_solat_api)
data = response.json()

# for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#     print(maklumat['time'])

def grab_api():
    waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
    response = requests.get(waktu_solat_api)
    data = response.json()
    print(data['data']['negeri'][0]['zon'][0]['waktu_solat'][0])
    return data

# def filter_results():
#     for info in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#         nama = info['name']
#         waktu = info['time']
#         if info['name'] == waktu_solat_api:
#             print(f'Waktu {nama} adalah pada: {waktu}')

grab_api()

#--------------------------------------------------------------------------------------
# '''
# ###############
# # PSEUDO CODE #
# ###############

# - grab_api()
#     - ambik API
#     - ambik "data" from .JSON
#     - release "data"

# - get_input()
#     - input_1 = Negeri
#     - input_2 = Daerah
#     - input_3 = Waktu
#     - release "Negeri", "Daerah", "Waktu"

# - filter_result()
#     - ambik data dari "data"
#     - "Negeri", "Daerah", "Waktu" 
#             - python waktu_solat.py Negeri Daerah Waktu
#             - Print Waktu spesifik
#     - "Negeri", "Daerah"          
#             - python waktu_solat.py Negeri Daerah
#             - Print Waktu seluruh "Daerah"
#     - "Negeri"                    
#             - python waktu_solat.py Negeri
#             - "Sila tulis "Daerah"
#             - input "Daerah"
#             - Print Waktu seluruh "Daerah"
# '''