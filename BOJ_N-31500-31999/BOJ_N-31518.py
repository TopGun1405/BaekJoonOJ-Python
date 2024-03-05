def main():
    n = int(input())

    sevens = 0
    for _ in range(3):
        slots = list(map(int, input().split()))
        if 7 in slots:
            sevens += 1

    print(777 if sevens == 3 else 0)


if __name__ == "__main__":
    main()
