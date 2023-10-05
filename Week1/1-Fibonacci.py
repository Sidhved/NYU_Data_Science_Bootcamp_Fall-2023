def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a+b
        print(c)
        a=b
        b=c




if __name__=="__main__":
    n = input("Enter the number of elements to compute: ")
    print("Printing first ",n, " elements of fibonacci series")
    fib(int(n))