student_list= {
                "andy": True,
                "bob": False,
                "charlie": True,
                "debbie": True,
                "eddie": False
              }

waktu_solat= [
                {
                    "name": "imsak",
                    "time": "05:33"
                },
                {
                    "name": "subuh",
                    "time": "05:43"
                },
                {
                    "name": "syuruk",
                    "time": "06:58"
                },
                {
                    "name": "zohor",
                    "time": "13:08"
                },
                {
                    "name": "asar",
                    "time": "16:33"
                },
                {
                    "name": "maghrib",
                    "time": "19:15"
                },
                {
                    "name": "isyak",
                    "time": "20:30"
                }
            ]

# for name in student_list:
#     if student_list[name] == True:
#         print(name)

for waktu in waktu_solat:
    for name in waktu:
        nama = name['name']
        waktu = name['waktu']
        if name['name'] == "subuh":
            print(f'waktu {nama} adalah pada {waktu}')