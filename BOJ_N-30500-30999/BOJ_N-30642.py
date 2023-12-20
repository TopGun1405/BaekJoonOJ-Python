def main():
    N = int(input())
    mascot = input()
    K = int(input())

    if mascot == "annyong":
        print(K if K % 2 == 1 else K + (1 if K + 1 <= N else -1))
    else:
        print(K if K % 2 == 0 else K + (1 if K + 1 <= N else -1))


if __name__ == "__main__":
    main()
