def main():
    A, B = input(), input().split()
    for b in B:
        A = A.replace(b, b.lower())
    print(A)


if __name__ == "__main__":
    main()
