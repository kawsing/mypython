#-*- coding: utf-8 -*-
# print("conditions:條件式")
# n=input("請輸入正整數： ")
# n=int(n)
# if n>200:
#     print("數字大於於200")
# elif n>100:
#     print("數字大於100，小於200")
# else:
#     print("數字小於等於100")

print("簡易四則運算")
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
op=input("請輸入 + - * /: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(int(n1/n2))
else:
    print("不支援的運算符號")

