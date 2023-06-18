def main():
    a, b = map(int, input().split())
    A = -a + (a ** 2 - b) ** 0.5
    B = -a - (a ** 2 - b) ** 0.5
    if A > B:
        print(int(B), int(A))
    elif A < B:
        print(int(A), int(B))
    else:
        print(int(A))


if __name__ == "__main__":
    main()
