def main():
    n, r = map(int, input().split())
    salaries = [int(input()) for _ in range(n)]

    inc = [0, 0]
    for salary in salaries:
        if salary + r > salary * 2:
            inc[0] += 1
        elif salary + r < salary * 2:
            inc[1] += 1

    print(1 if inc[0] > inc[1] else (2 if inc[0] < inc[1] else 0))


if __name__ == "__main__":
    main()
