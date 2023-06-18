def main():
    n = int(input())
    s = input()
    stayAwake, coffee = 0, 0
    for si in s:
        if si == '1':
            stayAwake += 1
            coffee = 2
        else:
            if coffee > 0:
                stayAwake += 1
                coffee -= 1
    print(stayAwake)


if __name__ == "__main__":
    main()
