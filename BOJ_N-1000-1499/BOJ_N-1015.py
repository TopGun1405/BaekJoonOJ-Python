def main():
    N = int(input())
    A = list(enumerate(map(int, input().split())))

    B = {val: idx for idx, val in enumerate(sorted(A, key=lambda k: k[1]))}
    P = [B[Ai] for Ai in A]
    print(*P)


if __name__ == "__main__":
    main()
