def main():
    n, m = map(int, input().split())
    cnt = 0
    for _ in range(n):
        sol = input()
        if '+' in sol:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
