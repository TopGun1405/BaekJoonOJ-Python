def main():
    while True:
        n = int(input())
        if n == 0:
            break
        pos = [int(input()) for _ in range(n)]
        print(*pos[::-1] + [0], sep='\n')


if __name__ == "__main__":
    main()
