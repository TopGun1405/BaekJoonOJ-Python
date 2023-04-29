def main():
    N, M = map(int, input().split())
    friends = {n: 0 for n in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A] += 1
        friends[B] += 1
    for num in friends:
        print(friends[num])


if __name__ == "__main__":
    main()
