def EvenOrOdd(n):
    return n%2==0

if __name__ == "__main__":
    for i in range(1,16):
        if EvenOrOdd(i):
            print(i, " : Even")
        else:
            print(i, " : Odd")