# 有序可變動列表 List
grades=[12,60,25,70,90]
print(grades)
print(grades[0])
print(grades[3])
print(grades[1:4])
grades=[12,60,25,70,90]
grades[0]=55 # 把 55 放到列表中的第一個位置
print(grades)
grades=[12,60,25,70,90]
grades[1:4]=[] # 連續刪除列表中從編號 1 到編號 4(不包括) 的資料
print(grades)
grades=[12,60,25,70,90]
grades=grades+[12,33]
print(grades)
grades=[12,60,25,70,90] # 取得列表的長度 len(列表資料)
length=len(grades)
print(length)
data=[[3,4,5],[6,7,8]]
print(data[0])
print(data[0][1])
print(data[0][0:2])
print(data)
data[0][0:2]=[5,5,5]
print(data)
# 有序不可變動列表 Tuple
data=(3,4,5)
# data[0]=5 # 錯誤︰Tuple的資料不可以變動
print(data[2])
print(data[0:2])