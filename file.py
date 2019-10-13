#-*- coding:utf-8 -*-
#檔案讀寫
print("檔案讀寫 : open and with open")
file=open("file.txt", mode="w", encoding="utf-8")
file.write("第一行\n第二行")
file.close()

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("100\n60")

with open("data.txt", mode="r", encoding="utf-8") as file:
    value=file.read()
print(value)

with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        print(line)

#把data.txt中的數字相乘
product=1
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        product*=int(line)
print(product)