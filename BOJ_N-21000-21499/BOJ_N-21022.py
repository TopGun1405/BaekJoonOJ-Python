def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    tot = 0
    for Ai, Bi in zip(A, B):
        if Ai > Bi:
            tot += 3
        elif Ai == Bi:
            tot += 1
    print(tot)


if __name__ == "__main__":
    main()
