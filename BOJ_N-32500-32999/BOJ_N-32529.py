def main():
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))[::-1]

    diet = [0] * (N+1)
    for i in range(1, N+1):
        diet[i] = diet[i-1] + A[i]

    if diet[-1] < M:
        print(-1)
    else:
        for i in range(1, N+1):
            if diet[i] >= M:
                print(N-i+1)
                break


if __name__ == "__main__":
    main()
