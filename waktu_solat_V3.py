from asyncio.windows_events import NULL
from operator import ne
from sqlite3 import DataError
from time import time
import requests
import sys

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()


# for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#     print(maklumat['time'])

# for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#     print(maklumat['name])

#------------------------------------------------------------------------

# print(data['data']) #this prints all

# for maklumat in data['about']:
#     print(maklumat) #this prints key in about

# for maklumat in data['data']:
#     print(maklumat) #this prints key in data

# for maklumat in data['data']['negeri']:
#     print(maklumat['nama']) #this prints list of negeri only

# for maklumat in data['data']['negeri']:
#     print(maklumat['zon']) #this prints list of every zon-name-time

# for maklumat in data['data']['negeri'][0]['zon']:
#     print(maklumat['nama']) #this prints list of zon only

# for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#     print(maklumat['name']) #this prints list of nama waktu solat

# for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#     print(maklumat['time']) #this prints list of pukul berapa solat
#------------------------------------------------------------------------

# print(data['data']) #this prints all

# for maklumat in data['about']:
#     print(maklumat) #this prints key in about

# for maklumat in data['data']:
#     print(maklumat) #this prints key in data

# for maklumat in data['data']['negeri']:
#     print(maklumat) #this prints list of every negeri-zon-name/time

# for maklumat in data['data']['negeri'][0]['zon']:
#     print(maklumat) #this prints list of every zon-name/time in specific negeri

# for maklumat in data['data']['negeri'][0]['zon'][0]:
#     print(maklumat) #this prints keys in zon

zon_input = 'mersing'

# for maklumat in data['data']['negeri'][0]['zon']:
#     if zon_input == waktu_solat_api:
#         print(maklumat) # this prints list of nama waktu solat and pukul berapa solat in specific zone
#     else:
#         print("Cuba lagi")

# for maklumat in data['data']['negeri'][0]['zon']:
#     print(maklumat)



# for maklumat in data['data']['negeri'][0]['zon']:
#     # nama = maklumat['name']
#     # waktu = maklumat['time']
#     if input_nama == maklumat['waktu_solat']:
#         print(f'Waktu {nama} adalah pada: {waktu}')

# for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
#     nama_waktu = maklumat['name']
#     pukul_berapa = maklumat['time']
#     if maklumat['name'] == input_nama:
#         print(maklumat['name'], maklumat['time'])
def get_input():
    input_nama_negeri = input("negeri: ")
    input_nama_zon = input("daerah: ")
    input_nama = input("waktu: ")
    return input_nama_negeri, input_nama_zon, input_nama

def First_Filter(input_nama_negeri):
    for maklumat in data['data']['negeri']:
        nama = maklumat['nama']
        zon = maklumat['zon']
        if maklumat['nama'] == input_nama_negeri:
            print(nama, zon)

def Second_Filter(input_nama_zon):
    for maklumat in data['data']['negeri'][0]['zon']:
        nama = maklumat['nama']
        waktu = maklumat['waktu_solat']
        if maklumat['nama'] == input_nama_zon:
            print(nama, waktu)

def Final_Filter(input_nama):
    for maklumat in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
        nama = maklumat['name']
        waktu = maklumat['time']
        if maklumat['name'] == input_nama:
            print(f'Waktu {nama} adalah pada pukul {waktu}')

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------

input_nama_negeri, input_nama_zon, input_nama = get_input()
Final_Filter(input_nama)

#------------------------------------------------------------------------
# def grab_api():
#     waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
#     response = requests.get(waktu_solat_api)
#     data = response.json()
#     return data

# def get_input():
#     negeri = sys.argv[1]
#     daerah = sys.argv[2]
#     waktu  = sys.argv[3]
#     # print(f'Negeri: {negeri} Daerah: {daerah} Waktu: {waktu}')
#     return str(negeri), str(daerah), str(waktu)

# def get_input():
#     negeri = input("Masukkan negeri: ")
#     daerah = input("Masukkan daerah: ")
#     waktu = input("Masukkan waktu: ")
#     return str(negeri), str(daerah), str(waktu)

# def filter_results(negeri, daerah, waktu):
#     for info in data['data']['negeri'][0]['zon'][0]['waktu_solat']:
        # nama_waktu = info['name']
        # pukul_berapa = info['time']
        # if negeri == NULL & daerah == NULL & waktu == NULL:
        #     print(f'Waktu {nama_waktu} adalah pada: {pukul_berapa}')

# def filter_results():
#     for info in data['data']

# def filter_results(negeri, daerah, waktu):
#     for info in data['data']:
#         negeri_json = info['negeri']
#         for info in data['data']['negeri']:
#             daerah_json = info['daerah']
#             for info in data['data']['negeri']['daerah']:
#                 waktu_solat_json = info['waktu_solat']
#                 name = info['name']
#                 time = info['time']
#                 if negeri == negeri_json & daerah == daerah_json & waktu == waktu_solat_json:
#                     print(name + time)
#                 elif negeri == negeri_json & daerah == daerah_json & waktu == NULL:
#                     print(daerah_json)
#                 elif negeri == negeri_json & daerah == NULL & waktu == NULL:
#                     print(negeri_json)
#                 elif negeri == NULL & daerah == NULL & waktu == NULL:
#                     print(data)
#         # if negeri == negeri_json:
#         #     print(negeri_json)

# grab_api()
# def main():

#         negeri, daerah, waktu = get_input()
#         filter_results(negeri, daerah, waktu)

# main()

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

