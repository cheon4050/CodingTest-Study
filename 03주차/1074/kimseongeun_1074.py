N, r, c = map(int, input().split())

count = 0
while N != 0:
    N -= 1
    size = 2 ** N

    if r < size and c < size:
        count += 0

    elif r < size and c >= size:
        count += size * size
        c -= size

    elif r >= size and c < size:
        count += size * size * 2
        r -= size

    else:
        count += size * size * 3
        r -= size
        c -= size

print(count)