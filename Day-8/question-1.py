
# 1:Write a Decorator function to take input for any kind of function you want to build.
def fibo(arg):
    def fibo1():
        n = int(input("Enter any Number - "))
        arg(n)
    return fibo1

@fibo
def fibonacci(num):
    fib1 = 0
    fib2 = 1
    print('0')
    print('1')
    for i in range(1,num-1):
        fibon = fib1 + fib2
        fib1 = fib2
        fib2 = fibon
        print(fibon)

fibonacci()

