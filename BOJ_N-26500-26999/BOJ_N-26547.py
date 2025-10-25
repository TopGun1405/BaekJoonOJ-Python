def main():
    n = int(input())
    for _ in range(n):
        word = input()
        k = len(word)

        print(word)
        for i in range(1, k-1):
            print(word[i] + " "*(k-2) + word[-i-1+k])
        if k > 1:
            print(word[::-1])


if __name__ == "__main__":
    main()
