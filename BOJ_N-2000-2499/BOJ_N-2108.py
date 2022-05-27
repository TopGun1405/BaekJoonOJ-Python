def main():
    N = int(input())
    num = []
    tot = 0

    for _ in range(N):
        n = int(input())
        tot = tot + n
        num.append(n)

    num.sort()

    print(round(tot / N))

    print(num[N // 2])

    # must O(N)
    temp = [num[0]]
    element = temp[-1]
    count, frequency = 1, 0
    # [4001] or [None]
    for i in num[1:] + [4001]:
        if i == element:
            count = count + 1
        elif i != element:
            if count > frequency:
                temp.clear()
                temp.append(element)
                frequency = count
            elif count == frequency and element not in temp:
                temp.append(element)
            count = 1
        element = i

    if len(temp) > 1:
        print(temp[1])
    else:
        print(temp[0])

    print(num[N - 1] - num[0])


if __name__ == "__main__":
    main()
