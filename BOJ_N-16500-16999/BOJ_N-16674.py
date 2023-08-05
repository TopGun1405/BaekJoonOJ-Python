def main():
    N = list(map(int, input()))
    n2018 = {
        2: 0,
        0: 0,
        1: 0,
        8: 0
    }

    for n in N:
        try:
            n2018[n] += 1
        except KeyError:
            print(0)
            break
    else:
        if len(list(filter(lambda e: e > 0, n2018.values()))) == 4:
            if n2018[2] == n2018[0] == n2018[1] == n2018[8]:
                print(8)
            else:
                print(2)
        else:
            print(1)


if __name__ == "__main__":
    main()
