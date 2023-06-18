def main():
    N = int(input())
    cnt = 0
    for _ in range(N):
        n = int(input())
        if n > 1:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
