def main():
    N = int(input())

    n = "%.250f" % 2 ** -N
    k = len(n)
    for i in range(k-1, 1, -1):
        if n[i] != "0":
            k = i
            break

    print(n[:k+1])


if __name__ == "__main__":
    main()
