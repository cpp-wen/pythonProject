from random import randint
def fac(num):
    result =1
    for n in range(1,num+1):
        result *= n
    return result

m = int(3)
n = int(2)
print(fac(m)//fac(n))


def roll_dice(n=1):
    total=0
    for _ in range(n):
        # _ 表示这个变量在方法内部没有使用 不关心 直接使用_表示就可以了
        total+=randint(1,6)
    return total

def add(a=0,b=0,c=0):
    return a+b+c

# 没有函数的重载直接进行方法显式声明的调用 或者直接调用
print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1,2))
# 显式命名声明了函数内容
print(add(c=50,a=100,b=2))