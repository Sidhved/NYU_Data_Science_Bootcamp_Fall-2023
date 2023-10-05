def Vowel(S):
    V = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in S:
        if i.lower() in V:
            count += 1
    return count

if __name__ == "__main__":
    S = input("Enter a word: ")
    print("Number of vowels in ", S, " are ", Vowel(S))
    