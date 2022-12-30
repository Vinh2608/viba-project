import requests
import json
import re
import os
    
# api-endpoint
URL = "http://localhost:8000/translate/vi_ba"
  
# location given here

data = ""
path_vi = "Kriem_vi/"
path_ba = "Kriem_ba/"
result = ""
folder_vi = []
file_name_vi = "Kriem_63.txt"
file_new = open(os.path.join("Kriem_result/", file_name_vi), 'w', encoding = 'utf-8')
with open(os.path.join(path_vi, file_name_vi),  encoding = 'utf-8') as f1:
    lines1 = f1.readlines()
    for line1 in lines1:
        if (line1 == "\n"):
            continue
        if "\n" in line1:
            line1 = line1.translate(str.maketrans('', '', "\n"))
        one_strip = line1.strip("\n")
        # print(one_strip)
        data = {"text": one_strip, "model":"BART_CHUNK"}
        r = requests.post(url = URL, json = data)
        result = r.json()
        print(result)
        file_new.write(result['src'].strip('\n') + "|" + result['tgt'] + "\n")
    # file_new.write("----------\n")
    # for line1 in lines1:
    #      file_new.write(line1)
file_new.close()