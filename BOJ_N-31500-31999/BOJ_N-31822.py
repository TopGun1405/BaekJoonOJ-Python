def main():
    code = input()
    N = int(input())
    C = [input() for _ in range(N)]

    cnt = 0
    for C_i in C:
        if code[:5] == C_i[:5]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
