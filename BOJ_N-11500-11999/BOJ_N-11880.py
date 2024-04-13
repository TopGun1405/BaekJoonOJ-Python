def main():
    T = int(input())
    for _ in range(T):
        a, b, c = map(int, input().split())
        A = a**2 + (b+c)**2
        B = b**2 + (c+a)**2
        C = c**2 + (a+b)**2
        print(min(A, B, C))


if __name__ == "__main__":
    main()
