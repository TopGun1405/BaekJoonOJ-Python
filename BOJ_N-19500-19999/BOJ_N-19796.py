def main():
    m, n = map(int, input().split())
    covered = [False] * (m + 1)
    for _ in range(n):
        l_i, r_i = map(int, input().split())
        for i in range(l_i, r_i + 1):
            covered[i] = True

    print("YES" if all(covered[1:]) else "NO")


if __name__ == "__main__":
    main()
