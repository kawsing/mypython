#-*- coding: utf-8 -*-
import urllib.request as request
import json
#連接網路，提取原始碼
# src="http://www.tn.edu.tw"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)
#使用JSON，取得opendata資料
#台南美食 https://www.twtainan.net/data/shops_zh-tw.json
src="https://www.twtainan.net/data/shops_zh-tw.json" #經觀察，這是一個列表資料
with request.urlopen(src) as response:
    #取得列表所有資料，裡面是字典格式
    data=json.load(response)
    #提取列表中所有資料，並依字典索引取得店名，地址與簡介
with open("台南美食.txt", mode="w") as file:
    for result in data:
        #print(result)
        info="店名："+result["name"]+" 地址："+result["address"]+"\n簡介："+result["introduction"]+"\n"
        print(info)
        #寫入資料
        file.write(info)