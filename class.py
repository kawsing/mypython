#-*- coding: utf-8 -*-
#類別與封裝的屬性
class  Test:
    x=3
    def say():
        print("Hello!")

class IO:
    supportSrc=["python", "JS", "PHP"]
    def read(src):
        if src not in IO.supportSrc:
            print("Not support", src)
        else:
            print("You can use", src)

#呼叫類別屬性
print(Test.x+5)
Test.say()
IO.supportSrc
IO.read("JS")
IO.read("C++")