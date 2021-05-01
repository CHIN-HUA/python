#參數的預設資料
# def power(base,exp=0):
#     print(base**exp) // 27
# power(3,3)
# power(4)

#使用參數名稱對應
# def divide(n1,n2=1):
#     print(n1/n2)
# divide(5,10)
# divide(n2=10,n1=5)

#無限(不定)參數資料(tuple)
# def avg(*ns):
#     print(ns)
# avg(3,4)

# def avg(*ns):
#     sum=0
#     for x in ns:
#         sum+=x
#     print(sum/len(ns))  
# avg(3,4)
# avg(3,4,10,55)