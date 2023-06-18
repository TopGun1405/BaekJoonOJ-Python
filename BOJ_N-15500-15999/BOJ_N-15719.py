def main():
    N = int(input())
    c = sum(range(1, N))
    n = input().rstrip()
    calc = 0
    t = ''
    for i in n:
        if i.isdigit():
            t += i
        else:
            calc += int(t)
            t = ''
    calc += int(t)
    print(calc - c)


if __name__ == "__main__":
    main()
