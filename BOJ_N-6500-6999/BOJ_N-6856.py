def main():
    m = int(input())
    n = int(input())

    cnt = 0
    for a in range(1, m + 1):
        for b in range(1, n + 1):
            if a + b == 10:
                cnt += 1

    if cnt == 1:
        print(f"There is {cnt} way to get the sum 10.")
    else:
        print(f"There are {cnt} ways to get the sum 10.")


if __name__ == "__main__":
    main()
