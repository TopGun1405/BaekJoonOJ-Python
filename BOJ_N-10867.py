def main():
    N = int(input())
    num = list(map(int, input().split()))
    print(*sorted(set(num)), sep=' ')


if __name__ == "__main__":
    main()
