def main():
    n = int(input())

    cnt = 0
    for a in range(n):
        for b in range(a, n):
            c = n - (a + b)
            if c < b:
                break
            if b + a > c:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
