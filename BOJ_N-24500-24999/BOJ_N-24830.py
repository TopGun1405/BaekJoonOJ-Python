def main():
    n = int(input())
    prev = 1
    for _ in range(n):
        a, op, b = input().split()
        a, b = int(a), int(b)

        res = 0
        if op == "+":
            res = (a + b) - prev
        elif op == "-":
            res = (a - b) * prev
        elif op == "*":
            res = (a * b) ** 2
        elif op == "/":
            res = (a + (1 if a % 2 else 0)) // 2
        prev = res

        print(res)


if __name__ == "__main__":
    main()
