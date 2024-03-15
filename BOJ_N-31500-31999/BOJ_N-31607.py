def main():
    A = int(input())
    B = int(input())
    C = int(input())

    if A + B == C or B + C == A or C + A == B:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
