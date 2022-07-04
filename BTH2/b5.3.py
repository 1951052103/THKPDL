import math

#a = [0, 4, 12, 16, 16, 18, 24, 26, 28]
a = [3, 5, 11, 12, 20, 24]
a.sort()

start = 0
start_value = a[0]
end_value = a[0]
k = 2

if(k > 0):
    result = []
    temp = []

    for i in range(len(a)):
        temp.append(a[i])
        if i + 1 < len(a):
            if i == start + k - 1:
                end_value = math.ceil((a[i] + a[i+1]) / 2)
                print('[{}, {})'.format(start_value, end_value))
                start = i + 1
                start_value = end_value

                result.append(temp)
                temp = []
        else:
            end_value = a[i]
            print('[{}, {}]'.format(start_value, end_value))
            result.append(temp)

print(result)