def main():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        for _ in range(H):
            Meats = input()
            print(Meats[::-1])


if __name__ == "__main__":
    main()
