def main():
    S = input()
    q = int(input())

    n = len(S)
    prefix = [[0] * 26 for _ in range(n+1)]
    for i in range(1, n+1):
        c = ord(S[i-1]) - 97
        prefix[i] = prefix[i-1][:]
        prefix[i][c] += 1

    for _ in range(q):
        a_i, l_i, r_i = map(lambda e: int(e) if e.isdigit() else e, input().split())

        c = ord(a_i) - 97
        print(prefix[r_i+1][c] - prefix[l_i][c])


if __name__ == "__main__":
    main()
