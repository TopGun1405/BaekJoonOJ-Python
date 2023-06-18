def main():
    A = int(input())
    B, C, D = int(input()), int(input()), int(input())
    P = int(input())
    m = A * P
    if C < P:
        n = B + ((P - C) * D)
    else:
        n = B
    print(min(m, n))


if __name__ == "__main__":
    main()
