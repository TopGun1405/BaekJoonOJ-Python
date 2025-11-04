def main():
    T = int(input())
    C = int(input())
    chores = sorted([int(input()) for _ in range(C)])

    cnt = 0
    for i in range(C):
        T -= chores[i]
        if T < 0:
            break
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
