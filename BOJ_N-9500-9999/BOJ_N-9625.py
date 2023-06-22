def main():
    K = int(input())
    A, B = 0, 1
    for _ in range(K-1):
        A, B = B, A + B
    print(A, B)


if __name__ == "__main__":
    main()
