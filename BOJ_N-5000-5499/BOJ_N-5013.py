def main():
    n = int(input())
    cnt = 0
    for _ in range(n):
        abilities = input()
        if abilities[-2:] != "CD":
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
