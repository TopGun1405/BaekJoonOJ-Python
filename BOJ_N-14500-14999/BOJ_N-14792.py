from collections import Counter


def main():
    T = int(input())
    for x in range(1, T+1):
        N, K = map(int, input().split())

        cnt = Counter()
        cnt[N] = 1
        l, r = 0, 0
        while K > 0:
            length = max(cnt)
            c = cnt[length]
            del cnt[length]

            l, r = (length - 1) // 2, length // 2

            K -= c
            cnt[l] += c
            cnt[r] += c

        y, z = max(l, r), min(l, r)

        print(f"Case #{x}: {y} {z}")


if __name__ == "__main__":
    main()
