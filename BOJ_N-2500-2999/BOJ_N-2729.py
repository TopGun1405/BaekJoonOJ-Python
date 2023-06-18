def main():
    T = int(input())
    for _ in range(T):
        a, b = input().split()
        a, b = int(a, 2), int(b, 2)
        print(bin(a + b)[2:])


if __name__ == "__main__":
    main()
