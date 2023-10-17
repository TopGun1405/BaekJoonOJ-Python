def main():
    rev = {
        'd': ['', 'q', 'b'],
        'b': ['', 'p', 'd'],
        'q': ['', 'd', 'p'],
        'p': ['', 'b', 'q']
    }

    N, D = map(int, input().split())
    for _ in range(N):
        S = input()
        print(*map(lambda s: rev[s][D], S), sep='')


if __name__ == "__main__":
    main()
