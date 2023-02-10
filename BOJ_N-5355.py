def main():
    T = int(input())
    for _ in range(T):
        op = input().split()
        ans = float(op[0])
        for i in range(1, len(op)):
            ans = ans * 3 if op[i] == '@' else (ans + 5 if op[i] == '%' else ans - 7)
        print('%0.2f' % ans)


if __name__ == "__main__":
    main()
