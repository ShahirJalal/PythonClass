data = {"air",
       {"makanan": ["buah", 
                   {"sayur":[{"kobis": ["india", "africa", "cina"]}, 
                    "saderi", 
                    "bayam", 
                    "kailan"]}
                   ]
            }
}

input_sayur = 'india'

for arkib in data["makanan"]['sayur']:
    nama1 = arkib['kobis']
    if input_sayur == nama1:
        print(arkib)