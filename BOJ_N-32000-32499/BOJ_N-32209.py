def main():
    Q = int(input())

    prob = 0
    for _ in range(Q):
        A, B = map(int, input().split())
        if A == 1:
            prob += B
        elif A == 2:
            prob -= B

        if prob < 0:
            print("Adios")
            break
    else:
        print("See you next month")


if __name__ == "__main__":
    main()
