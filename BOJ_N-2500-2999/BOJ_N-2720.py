def main():
    T = int(input())
    money, c = [25, 10, 5, 1], [0] * 4
    for _ in range(T):
        C = int(input())
        for i in range(4):
            c[i] = C // money[i]
            C %= money[i]
        print(*c)


if __name__ == "__main__":
    main()
