num = [1,2,'3']
sum = 0
for n in num:
    if n% 2 == 0:
        sum += n
    else:
        sum -= n
print(sum)