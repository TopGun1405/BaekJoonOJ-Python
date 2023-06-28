def main():
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)
    print(sum(a[::2]), sum(a[1::2]))


if __name__ == "__main__":
    main()
