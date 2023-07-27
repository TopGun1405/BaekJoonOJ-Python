# import sys
# input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = [input().split() for _ in range(N)]
    B = [input().split() for _ in range(N)]

    AA = [int(''.join(a), 2) for a in A]
    BB = [int(''.join(B[r][c] for r in range(N)), 2) for c in range(N)]
    res = 0
    for Ai in AA:
        for Bi in BB:
            if Ai & Bi:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
