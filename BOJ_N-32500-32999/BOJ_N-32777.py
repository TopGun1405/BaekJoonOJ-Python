def main():
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())

        if a >= b:
            inner, outer = 43-(a-b), a-b
        else:
            inner, outer = b-a, 43-(b-a)

        if inner < outer:
            print("Inner circle line")
        elif inner > outer:
            print("Outer circle line")
        else:
            print("Same")


if __name__ == "__main__":
    main()
