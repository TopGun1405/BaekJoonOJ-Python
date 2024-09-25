def main():
    N, K = map(int, input().split())
    T = list(input())

    for i in range(K-1, N):
        T[i] = T[i].lower() if T[i].isupper() else T[i].upper()

    print("".join(T))


if __name__ == "__main__":
    main()
