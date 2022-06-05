a, b, c = map(int, input().split())

count = 0
num_start = a
while num_start <= b:
    if c % num_start == 0:
        count += 1
    num_start += 1

print(count)
