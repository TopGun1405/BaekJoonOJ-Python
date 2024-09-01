def main():
    N, K = map(int, input().split())
    AD = []
    for _ in range(N):
        A, B = map(int, input().split())
        AD.append(B - A)
    AD.sort()

    print(AD[K-1] if AD[K-1] >= 0 else 0)


if __name__ == "__main__":
    main()
