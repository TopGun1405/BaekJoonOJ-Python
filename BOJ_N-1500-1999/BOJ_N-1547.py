def main():
    cup = [1, 2, 3]
    M = int(input())
    for _ in range(M):
        x, y = map(int, input().split())
        xi = cup.index(x)
        yi = cup.index(y)
        cup[xi], cup[yi] = cup[yi], cup[xi]
    print(cup[0])


if __name__ == "__main__":
    main()
