def main():
    S = list(input())
    T = list(input())

    while T:
        c = T.pop()
        if c == 'B':
            T = T[::-1]
        if S == T:
            print(1)
            break
    else:
        print(0)


if __name__ == "__main__":
    main()
