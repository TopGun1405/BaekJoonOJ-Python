def main():
    n = int(input())
    for _ in range(n):
        UG, US, UB, RG, RS, RB = map(int, input().split())
        USA, RUS = [UG, US, UB], [RG, RS, RB]
        color = USA > RUS
        count = sum(USA) > sum(RUS)

        print(*USA, *RUS)
        if color and count:
            print("both")
        elif color and not count:
            print("color")
        elif not color and count:
            print("count")
        else:
            print("none")
        if _ < n - 1:
            print()


if __name__ == "__main__":
    main()
