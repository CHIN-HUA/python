#a044: 空間切割

while True:
    try:
        n = int(input())
        print((n * n * n + 5 * n + 6) // 6)

    except(EOFError):
        pass
