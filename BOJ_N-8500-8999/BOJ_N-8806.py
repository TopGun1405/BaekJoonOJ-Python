def main():
    Z = int(input())
    for _ in range(Z):
        X1, Y1, Z1 = map(float, input().split())
        X2, Y2, Z2 = map(float, input().split())
        A = Z1*X2 + Y1*Z2 + X1*Y2
        G = Z2*X1 + Y2*Z1 + X2*Y1
        print("ADAM" if A > G else ("GOSIA" if G > A else '='))


if __name__ == "__main__":
    main()
