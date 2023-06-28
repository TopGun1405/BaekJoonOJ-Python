def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(*sorted(A + B), sep='\n')


if __name__ == "__main__":
    main()
