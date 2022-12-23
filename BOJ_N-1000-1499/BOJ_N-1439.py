def main():
    S = input()
    cnt, temp = 0, ' '
    for i in S:
        if i != temp:
            cnt, temp = cnt + 1, i
    print(cnt // 2)


if __name__ == "__main__":
    main()
