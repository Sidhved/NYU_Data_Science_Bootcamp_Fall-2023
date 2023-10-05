def Sum(A):
    return A[0]+A[-1]

if __name__ == "__main__":
    print("Give 2 values to add")
    A = list(map(float, input().split()))
    print(round(Sum(A),2))
