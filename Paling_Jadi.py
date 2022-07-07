import sys
import requests

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()


###############
##   INPUT   ##
###############

# input_negeri = 'johor'
# input_zon    = 'mersing'
# input_waktu  = 'isyak'

# def get_input():
# input_negeri = sys.argv[1]
# input_zon    = sys.argv[2]
# input_waktu  = sys.argv[3]
# return input_negeri, input_zon, input_waktu

# replace_negeri= sys.argv[1]
# input_negeri = replace_negeri.replace("_", " ")
# replace_zon    = sys.argv[2]
# input_zon = replace_zon.replace("_", " ")
# replace_waktu  = sys.argv[3]
# input_waktu = replace_waktu.replace("_", " ")

input_negeri = input("Sila masukkan nama negeri: ")
input_zon = input("Sila masukkan nama zon: ")
input_waktu = input("Sila masukkan nama waktu: ")


###############
##  FILTER   ##
###############

# def data_filter(input_negeri, input_zon, input_waktu):
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



# def main():

#                         break
#                 else:
#                     print(info['waktu_solat'])
#                     break
#         else:
#             print(arkib['zon'])
#             break
# else:
#     print(data['data']['negeri'])
