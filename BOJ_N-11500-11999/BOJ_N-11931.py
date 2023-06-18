def main():
    N = int(input())
    num = [int(input()) for _ in range(N)]
    print(*sorted(num, reverse=True), sep='\n')


if __name__ == "__main__":
    main()
