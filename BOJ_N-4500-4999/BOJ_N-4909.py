def main():
    while True:
        grades = sorted(map(int, input().split()))
        if sum(grades) == 0:
            break
        grades = grades[1:-1]
        tot = sum(grades)
        print(tot / 4 if tot % 4 else int(tot / 4))


if __name__ == "__main__":
    main()
