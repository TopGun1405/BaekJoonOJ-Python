def main():
    N = int(input())
    num = [int(input()) for _ in range(N)]
    print(*sorted(num), sep='\n')


if __name__ == "__main__":
    main()
