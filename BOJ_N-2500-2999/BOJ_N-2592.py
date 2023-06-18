def main():
    num = dict()
    for _ in range(10):
        n = int(input())
        if n in num:
            num[n] += 1
        else:
            num.update({n: 1})

    tot, m, temp = 0, 0, 0
    for i in num:
        tot += i * num[i]
        if num[i] > temp:
            m, temp = i, num[i]
    print(tot // 10)
    print(m)


if __name__ == "__main__":
    main()
