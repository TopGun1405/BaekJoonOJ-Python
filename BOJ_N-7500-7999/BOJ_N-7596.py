def main():
    i = 1
    while True:
        n = int(input())
        if n == 0:
            break
        songs = sorted([input() for _ in range(n)])
        print(i)
        print(*songs, sep='\n')
        i += 1


if __name__ == "__main__":
    main()
