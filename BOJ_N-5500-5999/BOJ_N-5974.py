def main():
    L, C, N = map(int, input().split())
    for _ in range(C):
        S, P = map(int, input().split())

        print(abs(P - N) + S)


if __name__ == "__main__":
    main()
