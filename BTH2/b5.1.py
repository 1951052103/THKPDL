import statistics
import math


arr = [6, 2.5, 5.1, 5.1, 1]
arr.sort()

tb = sum(arr) / len(arr)
tv = statistics.median(arr)
mode = statistics.mode(arr)
ps = statistics.variance(arr, xbar=None) # Phương sai
dlc = math.sqrt(ps) # Độ lệch chuẩn

print(arr)
print('Giá trị trung bình: ' + str(tb))
print('Giá trị trung vị: ' + str(tv))
print('Giá trị mode: ' + str(mode))
print('Độ lệch chuẩn: ' + str(dlc))