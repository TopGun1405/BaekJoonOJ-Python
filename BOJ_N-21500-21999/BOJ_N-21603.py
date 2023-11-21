def main():
    N, K = map(int, input().split())
    fK, f2K = K % 10, (2 * K) % 10

    f = [x for x in range(1, N + 1) if x % 10 != fK and x % 10 != f2K]
    print(len(f))
    print(*f)


if __name__ == "__main__":
    main()
