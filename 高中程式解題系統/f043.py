#f043: 1. 小豪的回家作業 (Homework)

x, y = map(int, input().split())
if x > y: #5 4
    num = x - y #1
    if y > num:
        print(num,"+",y,"=",x,sep='')
    else:
        print(y,"+",num,"=",x,sep='')
elif x == y: #4 4 // 6 6
    num = y - 3
    x = x - num
    if num < x:
        print(num,"+",x,"=",y,sep='')
    else:
        print(x,"+",num,"=",y,sep='')
