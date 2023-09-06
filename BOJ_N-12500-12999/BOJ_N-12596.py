def main():
    N = int(input())
    for n in range(1, N + 1):
        G = int(input())
        C = list(map(int, input().split()))
        c = list(filter(lambda e: C.count(e) == 1, C))
        print(f'Case #{n}: {c[0]}')


if __name__ == "__main__":
    main()
