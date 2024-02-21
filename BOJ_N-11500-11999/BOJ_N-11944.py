def main():
    N, M = map(int, input().split())
    NN = str(N) * N
    print(NN if len(NN) <= M else NN[:M])


if __name__ == "__main__":
    main()
