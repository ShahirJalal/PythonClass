import requests


waktu_solat_api = "https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json"
response = requests.get(waktu_solat_api)
data = response.json()

# for info in data['data']:
#     for negeri in info['negeri']:
#         print(negeri)

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'Physics']}

# for data in student:
#     print(data)

for data in student:
    for courses in data['courses']:
        i = 1
        i + 1
        while i <= len(data['courses']):
            print(courses)

# print(student['courses'][0])