def main():
    N, M = map(int, input().split())
    for n in range(N):
        if n % 2:
            for m in range(M):
                print('*' if m % 2 else '.', end='')
        else:
            for m in range(M):
                print('.' if m % 2 else'*', end='')
        print()


if __name__ == "__main__":
    main()
