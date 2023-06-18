def main():
    a, b, n = map(int, input().split())
    dCnt = 0
    for k in range(a, b + 1):
        dCnt += str(k).count(str(n))
    print(dCnt)


if __name__ == "__main__":
    main()
