# class Point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x, self.y)
#     def distance(self,tpx, tpy):
#         return (((self.x-tpx)**2)+((self.y-tpy)**2))**0.5
# p=Point(3, 5)
# print(p.x,p.y) 
# p2=Point(7,5)
# print(p2.x, p2.y)
# p3=Point(9,2)
# p3.show()
# p4=Point(5,6)
# result=p4.distance(0,0)
# print(result)

class File:
    def __init__(self, name):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
f=File("data.txt")
f.open()
data=f.read()
print(data)
    