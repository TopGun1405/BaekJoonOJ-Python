def main():
    T = int(input())
    for _ in range(T):
        N = int(input())

        if N <= 5:
            print("MIT time")
        else:
            for k in range(2, 14):
                if 5**(k-1) < N <= 5**k:
                    print(f"MIT^{k} time")
                    break


if __name__ == "__main__":
    main()
