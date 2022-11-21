def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        if A ** 2 - (A - 1) ** 2 > N:
            break
        for B in range(1, A + 1):
            if A ** 2 - B ** 2 == N:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
