def main():
    N = int(input())
    A = list(map(int, input().split()))
    X, Y = map(int, input().split())

    numA = [Ai for Ai in A if Ai >= Y]
    print(round(N * (X / 100)), len(numA))


if __name__ == "__main__":
    main()
