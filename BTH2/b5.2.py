import math

a = [3, 5, 11, 12, 20, 24]
a.sort()

min = min(a)
max = max(a)

k = 4

if(k > 0):
    size = math.ceil((max - min) / k)

    kq = []
    temp = []
    for i in range(k):
        if min + size < max:
            print('[{}, {})'.format(min, min + size))

            for j in a:
                if j < min:
                    continue
                elif min <= j < min + size:
                    temp.append(j)
                elif j >= min + size:
                    break
            kq.append(temp)
            temp = []

            min += size
        else:
            print('[{}, {}]'.format(min, max))

            for j in a:
                if j < min:
                    continue
                elif min <= j <= max:
                    temp.append(j)
            kq.append(temp)

print(kq)