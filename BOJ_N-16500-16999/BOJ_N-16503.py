def calc(n, m, op):
    if op == '+':
        return n + m
    elif op == '-':
        return n - m
    elif op == '*':
        return n * m
    elif op == '/':
        return -(abs(n) // abs(m)) if n * m < 0 else n // m


def main():
    num1, op1, num2, op2, num3 = input().split()
    num1, num2, num3 = int(num1), int(num2), int(num3)
    p = calc(calc(num1, num2, op1), num3, op2)
    q = calc(num1, calc(num2, num3, op2), op1)
    print(min(p, q))
    print(max(p, q))


if __name__ == "__main__":
    main()
