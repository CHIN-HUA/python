#n = 0
#for x in [0, 1, 2, 3]:
#    if x%2==0:
#        continue
#    n+=1
#print(n) #//印出2

#break簡易範例
# n = 0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print("最後的 n:", n)

#continue 簡易範例
# n = 0
# for x in [0, 1, 2, 3]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("最後的 n:", n)

# #else 範例
# sum = 0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) # 1 + 2 + .... + 10

n = input("輸入一個正整數: ")
n = int(n)
for i in range(n): # i ==> 0 ~ n-1
    if(i * i == n):
        print("整數平方根", i)
        break # 強制結束迴圈，不會執行else 區域2
else:
    print("沒有整數平方根")
