import sys
import requests

waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()


if len(sys.argv) == 4:
    input_negeri = sys.argv[1]
    input_zon    = sys.argv[2]
    input_waktu  = sys.argv[3]
elif len(sys.argv) == 3:
    input_negeri = sys.argv[1]
    input_zon    = sys.argv[2]
    input_waktu  = ''
elif len(sys.argv) == 2:
    input_negeri = sys.argv[1]
    input_zon    = ''
    input_waktu  = ''
elif len(sys.argv) == 1:
    input_negeri = ''
    input_zon    = ''
    input_waktu  = ''

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
                        break
                else:
                    print(info['waktu_solat'])
                break
        else:
            print(arkib['zon'])
        break
else:
    print(data['data']['negeri'])
