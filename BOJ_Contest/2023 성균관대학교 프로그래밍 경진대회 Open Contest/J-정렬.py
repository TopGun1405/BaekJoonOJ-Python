from collections import deque


def main():
    N = int(input())
    A = {0: deque(map(int, input().split())), 1: deque()}
    sortedA = sorted(A[0])
    print(sortedA)
    while A[0] != sortedA:
        pass


if __name__ == "__main__":
    main()
