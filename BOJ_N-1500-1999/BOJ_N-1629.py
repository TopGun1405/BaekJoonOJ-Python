def main():
    # A**(m + n) = A**m + A**n
    # (A * B) % C = (A % C) * (B % C) % C
    def mult(k, n):
        if n == 1:
            return k % C
        num = mult(k, n // 2)
        if n % 2:
            return (num ** 2 * k) % C
        else:
            return num ** 2 % C

    A, B, C = map(int, input().split())
    print(mult(A, B))


if __name__ == "__main__":
    main()
