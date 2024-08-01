def main():
    n = int(input())
    table = {}
    for _ in range(n):
        c_i, w_i = input().split()
        table[c_i] = int(w_i)

    m = int(input())
    money = -10 * m
    for _ in range(m):
        c = input()
        try:
            money += table[c]
        except KeyError:
            pass

    print(money)


if __name__ == "__main__":
    main()
