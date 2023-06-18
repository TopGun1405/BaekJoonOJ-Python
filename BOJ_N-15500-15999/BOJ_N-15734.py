def main():
    L, R, A = map(int, input().split())
    m, n = min(L, R), max(L, R)
    temp = min(A, n - m)
    A -= temp
    ans = (m + temp) * 2 + (A // 2 * 2 if A else 0)
    print(ans)


if __name__ == "__main__":
    main()
