def main():
    N, M = map(int, input().split())
    friend = [0] * (N + 1)
    for i in range(M):
        A, B = map(int, input().split())
        friend[A] += 1
        friend[B] += 1

    for i in range(1, N + 1):
        print(friend[i])


if __name__ == "__main__":
    main()
