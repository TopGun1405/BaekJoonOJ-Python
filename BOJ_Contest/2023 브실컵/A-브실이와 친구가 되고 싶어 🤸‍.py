def main():
    A, B = map(int, input().split())
    K, X = map(int, input().split())
    friends = list(filter(lambda n: abs(n - K) <= X, range(A, B + 1)))
    print(len(friends) if friends else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
