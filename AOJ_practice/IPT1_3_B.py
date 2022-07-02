count = 0

while True:
    x = int(input())
    if x == 0:
        break
    else:
        count += 1
        print("Case " + str(count) + ": " + str(x))
