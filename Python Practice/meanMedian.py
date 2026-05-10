l1 = [6,8,4,9,3,10,8,11,5,7,8,4,2]
count = 0
mean = 0

for i in l1:
    count += 1
    mean += i   

mean = mean/count
print('Mean:', mean)

l1.sort()
if count % 2 == 0:
    median = (l1[count//2 - 1] + l1[count//2]) / 2  
else:
    median = l1[count//2]
print('Median:', median)