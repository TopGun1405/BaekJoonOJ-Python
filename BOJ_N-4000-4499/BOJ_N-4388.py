def main():
    while True:
        a, b = input().split()
        if a == b == '0':
            break
        A, B = len(a), len(b)
        if A > B:
            b = (A - B) * '0' + b
        else:
            a = (B - A) * '0' + a
        carry, nCarry = 0, 0
        for i in range(len(a) - 1, -1, -1):
            if int(a[i]) + int(b[i]) + carry >= 10:
                carry, nCarry = 1, nCarry + 1
            else:
                carry = 0
        print(nCarry)


if __name__ == "__main__":
    main()
