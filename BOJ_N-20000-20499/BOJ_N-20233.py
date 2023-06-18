def main():
    a, x, b, y = int(input()), int(input()), int(input()), int(input())
    T = int(input())
    op_1, op_2 = a + max(T - 30, 0) * x * 21, b + max(T - 45, 0) * y * 21
    print(op_1, op_2)


if __name__ == "__main__":
    main()
