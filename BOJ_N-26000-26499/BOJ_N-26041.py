def main():
    A = input().split()
    B = input()

    cnt = 0
    for A_i in A:
        if A_i != B and A_i[:len(B)] == B:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
