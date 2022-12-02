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
file_name_vi = "Kriem_75.txt"
file_new = open(os.path.join("Kriem_result/", file_name_vi), 'w', encoding = 'utf-8')
with open(os.path.join(path_vi, file_name_vi),  encoding = 'utf-8') as f1:
    lines1 = f1.readlines()
    for line1 in lines1:
        if (line1 == "\n"):
            continue
        if "\n" in line1:
            line1 = line1.translate(str.maketrans('', '', "\n"))
        one_strip = line1.strip(" \n-")
        print(one_strip)
        data = {"text": one_strip, "model":"BART_CHUNK"}
        r = requests.post(url = URL, json = data)
        result = r.json()
        print(result)
        file_new.write(line1 + "|" + result['tgt'] + "\n")
    # file_new.write("----------")
    # for line1 in lines1:
    #     file_new.write(line1)
file_new.close()
# for file_name_vi, file_name_ba in list(zip(os.listdir(path_vi), os.listdir(path_ba))):
#     print(file_name_vi, file_name_ba)
#     with open(os.path.join(path_vi, file_name_vi), encoding = 'utf-8') as f1, open(os.path.join(path_ba, file_name_ba), encoding = 'utf-8') as f2:
#         file_new = open(os.path.join("Kriem_result/", file_name_vi), 'w', encoding = 'utf-8')
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()
#         if (lines1[0] == "HỘI THOẠI.\n"):
#             for line1, line2 in list(zip(lines1, lines2)):
#                 if (line1 == "\n"):
#                     continue
#                 if "\n" in line1:
#                     line1 = line1.translate(str.maketrans('', '', "\n"))
#                 if "\n" in line2:
#                     line2 = line2.translate(str.maketrans('', '', "\n"))
#                 one_strip = line1.strip("- \n")
#                 print(one_strip)
#                 data = {"text": one_strip, "model":"BART_CHUNK"}
#                 r = requests.post(url = URL, json = data)
#                 result = r.json()
#                 file_new.write(result['tgt'] + '|' + line2 + "\n")
#         else:
#             for line1 in lines1:
#                 print(line1)
#                 if (line1 == "\n"):
#                     continue
#                 if "\n" in line1:
#                     line1 = line1.translate(str.maketrans('', '', "\n"))
#                 one_strip = line1.strip(" \n-")
#                 if (len(one_strip.split()) >= 7):
#                     data = {"text": one_strip, "model": "BART_CHUNK"}
#                 else:
#                     data = {"text": one_strip, "model":"BART_CHUNK"}
#                 r = requests.post(url = URL, json = data)
#                 result = r.json()
#                 file_new.write(result['tgt'] + "\n")
#             file_new.write("-------------\n")
#             for line in lines2:
#                 if (line == "\n"):
#                     continue
#                 file_new.write(line)

        



        
            


  
# defining a params dict for the parameters to be sent to the API
# file_content = f.read().replace('\n', ' ')
# file_content = re.split(".", file_content)
# print(file_content)
#data = f"{{\"text\": \"{file_content}\", \"model\": \"dictionary_translate\"}}"

  
# sending get request and saving the response as response object
#r = requests.post(url = URL, json = data)
  
# extracting data in json format
#data = r.json()
#result = data['ResultObj']['tgt'][0].replace("$", "\n")
#print(data['ResultObj']['tgt'][0])
#print(result)

#print(data)