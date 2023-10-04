def main():
    n = int(input())
    fileName = [input() for _ in range(n)]
    m = int(input())

    for _ in range(m):
        li, ri = map(int, input().split())
        print(*fileName[li-1:ri], sep='\n')


if __name__ == "__main__":
    main()
