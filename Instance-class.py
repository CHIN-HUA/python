#Point實體物件的設計: 平面座標的點
# class Point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
# #建立第一個實體物件
# p1=Point(3,4)
# print(p1.x, p1.y)
# #建立第二個實體物件
# p2=Point(5,6)
# print(p2.x, p2.y)

#FullName 實體物件的設計: 紀錄 姓, 名
class FullName:
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=FullName("C.w.", "Peng")
print(name1.first, name1.last)
name2=FullName("T.Y.", "Lin")
print(name2.first, name2.last)