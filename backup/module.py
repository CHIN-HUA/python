import sys
sys.path.append("modules") #在模組中的搜索路徑列表中 (新增路徑)

import sys as system
print(system.platform)
print(system.maxsize)

print("==========================")


#建立 geometry 模組, 載入使用
import geometry
result = geometry.distance(1, 1, 5, 5)
print(result)

result = geometry.slope(1, 2, 5, 6)
print(result)

print("==========================")

#模組的搜尋路徑
import sys
print(sys.path) #印出模組的搜索路徑

print("==========================")

import sys
sys.path.append("modules") #在模組中的搜索路徑列表中 (新增路徑)
print(sys.path)

print("---------------------------")
import geometry
print(geometry.distance(1, 1, 5, 5))






