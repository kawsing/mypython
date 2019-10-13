# -*- coding: utf-8 -*-
import json
#讀取資料
with open("config.json", mode="r") as file:
    info=json.load(file)
print(info) #python 字典檔
print(info["name"])
print(info["career"])

#變更字典檔資料
info["favorite"]="Computer"
print(info)
with open("config.json", mode="w") as file:
    json.dump(info, file)
