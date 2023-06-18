def main():
    N = int(input())
    m = 0
    for _ in range(N):
        dice = map(int, input().split())
        e = dict()
        for i in dice:
            if i in e:
                e[i] += 1
            else:
                e.update({i: 1})
        print(e)
        i = list(e.keys())
        if len(e) == 1:
            print(50000 + e[i[0]] * 5000)
        elif len(e) == 2:
            if len(set(e.values())) == 2:
                print()


if __name__ == "__main__":
    main()
