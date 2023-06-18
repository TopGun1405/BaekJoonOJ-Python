def main():
    P = int(input())
    for _ in range(P):
        N, D, A, B, F = map(float, input().split())
        T = D / (A + B) * F
        print("{} {:0.6f}".format(N, T))


if __name__ == "__main__":
    main()
