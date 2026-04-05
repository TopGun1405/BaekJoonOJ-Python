from collections import deque


def main():
    T = int(input())
    for x in range(1, T+1):
        N = int(input())
        P = deque(map(int, input().split()))

        d = []
        while P:
            p = P.popleft()
            if p * 100 // 75 in P:
                d.append(p)
                P.remove(p * 100 // 75)

        print(f"Case #{x}: {' '.join(map(str, d))}")


if __name__ == "__main__":
    main()
