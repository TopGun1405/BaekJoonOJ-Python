def main():
    n = int(input())
    # num = sorted(map(int, input().split()))
    # print(num[0] * num[-1] if n > 1 else num[0] ** 2)
    num = list(map(int, input().split()))
    print(max(num) * min(num) if n > 1 else num[0] ** 2)


if __name__ == "__main__":
    main()
