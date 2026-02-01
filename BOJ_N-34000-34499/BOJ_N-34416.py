def main():
    n = int(input())
    pos = int(input())
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        if pos == x:
            pos = y
        elif pos == y:
            pos = x
    
    print(pos)


if __name__ == "__main__":
    main()
