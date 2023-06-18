def main():
    n, T = map(int, input().split())
    num = list(map(int, input().split()))
    w = 0
    while True:
        if len(num) == 0:
            break
        elif T < num[0]:
            break
        T -= num.pop(0)
        w += 1
    print(w)


if __name__ == "__main__":
    main()
