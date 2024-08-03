def main():
    N = int(input())
    O = int(input())

    N -= 1
    P = O // N
    if O == P * N:
        print(O+P-1, O+P)
    else:
        print(O+P, O+P)


if __name__ == "__main__":
    main()
