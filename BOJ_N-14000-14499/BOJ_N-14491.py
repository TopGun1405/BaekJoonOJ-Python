def main():
    T = int(input())
    t = 0
    while 9 ** t <= T:
        t += 1
    res = ''
    for i in range(t - 1, -1, -1):
        res += str(T // (9 ** i))
        T = T % (9 ** i)
    print(res)


if __name__ == "__main__":
    main()
