def main():
    n = int(input())
    s = input()

    L, O = s.count("L"), s.count("O")
    myL, myO = 0, 0
    res = -1
    for i in range(1, n):
        if s[i-1] == "L":
            myL += 1
        else:
            myO += 1

        friendL, friendO = L-myL, O-myO
        if myL != friendL and myO != friendO:
            res = i

    print(res)


if __name__ == "__main__":
    main()
