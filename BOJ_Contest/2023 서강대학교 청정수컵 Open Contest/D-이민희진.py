from itertools import combinations


def main():
    N = int(input())
    names = list(combinations([input() for _ in range(N)], 2))
    connectable = 0
    for S, T in names:
        for k in range(min(len(S), len(T))):
            if S[-k-1:] == T[:k+1] or T[-k-1:] == S[:k+1]:
                connectable += 1
                break
    print(connectable)


if __name__ == "__main__":
    main()
