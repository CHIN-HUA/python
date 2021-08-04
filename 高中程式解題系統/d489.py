#d489: 伏林的三角地
import math 
x, y, z = map(int, input().split())

s = (x + y + z) / 2
num = (s * (s - x) *(s - y) *(s - z))

print(round(num))