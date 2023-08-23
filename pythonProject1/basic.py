"""
一些基础知识快速 过一下 记录一下
"""
import random
sum =0
for x in range(101):
    sum+=x
print(sum)

for x in range(2,101,2):
    sum+=x
print(sum)


answer = random.randint(1,100)
count =0
while False:
    count +=1
    number= int (input("shuru"))
    if number > answer:
        print("max")
    elif number<answer:
        print("min")
    else:
        print("yes")
        break
print(' count %d',count)
if count>8:
    print("you are bad")

# python 注释有点奇怪的
for i in  range(1,10):
    for j in range(1,i+1):
        print('i is  %d j is %d ',i,j)
    print()
