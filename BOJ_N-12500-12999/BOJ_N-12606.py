def main():
    N = int(input())
    for n in range(1, N + 1):
        L = input().split()
        print(f"Case #{n}: {' '.join(L[::-1])}")


if __name__ == "__main__":
    main()
