def main():
    n = int(input())
    k, minP = 1e4, 0
    for _ in range(n):
        pi = int(input())
        if pi <= k:
            k = pi
        else:
            minP += pi - k
    print(minP)


if __name__ == "__main__":
    main()
