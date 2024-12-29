def main():
    T = int(input())
    for _ in range(T):
        S = input()

        res = ""
        cnt, num = 0, S[0]
        for c in S:
            if num != c:
                res += str(cnt) + num
                cnt, num = 1, c
            else:
                cnt += 1
        res += str(cnt) + num

        print(res)


if __name__ == "__main__":
    main()
