def main():

    def rev(s):
        return s[::-1]

    def tail(s):
        return s[1:]

    iceCream3 = [lambda s, sp: s == sp + rev(sp) + sp,
                 lambda s, sp: s == sp + tail(rev(sp)) + sp,
                 lambda s, sp: s == sp + rev(sp) + tail(sp),
                 lambda s, sp: s == sp + tail(rev(sp)) + tail(sp)]

    T = int(input())
    for _ in range(T):
        S = input()

        n = len(S)
        Sp = S[:n//3+(1 if n % 3 else 0)]

        for check in iceCream3:
            if check(S, Sp):
                print(1)
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
