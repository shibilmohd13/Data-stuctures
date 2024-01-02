def sumrec(num):
    if num < 1:
        return 0
    else:
        return num + sumrec(num - 1)

print(sumrec(5))