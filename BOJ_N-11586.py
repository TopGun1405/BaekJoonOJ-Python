def main():
    N = int(input())
    mirror = [input() for _ in range(N)]
    K = int(input())
    if K == 1:
        print(*mirror, sep='\n')
    elif K == 2:
        for row in mirror:
            print(row[::-1])
    else:
        print(*mirror[::-1], sep='\n')


if __name__ == "__main__":
    main()
