def main():
    N = int(input())
    A = input()
    B = input()

    cnt, isSame = 0, True
    for a, b in zip(A, B):
        if a != b:
            isSame = False
        if not isSame and a == b:
            isSame = True
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
