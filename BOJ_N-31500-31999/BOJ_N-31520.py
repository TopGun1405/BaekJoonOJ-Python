def main():
    n = input()

    # c = "123456789"
    # print([-1, len(c)][n == c[:len(n)]])

    champWord, k = "", 1
    while len(champWord) < len(n):
        champWord += str(k)
        k += 1

    print(k-1 if champWord == n else -1)


if __name__ == "__main__":
    main()
