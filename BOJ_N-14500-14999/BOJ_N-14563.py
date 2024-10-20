def main():
    T = int(input())
    N = list(map(int, input().split()))

    for n_i in N:
        tot = 0

        for i in range(1, n_i):
            if n_i % i == 0:
                tot += i

        if tot == n_i:
            print("Perfect")
        elif tot > n_i:
            print("Abundant")
        elif tot < n_i:
            print("Deficient")


if __name__ == "__main__":
    main()
