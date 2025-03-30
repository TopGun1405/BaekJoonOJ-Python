def main():
    N = int(input())
    cnt = 0
    for _ in range(N):
        name = input()
        if name[0] == "C":
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
