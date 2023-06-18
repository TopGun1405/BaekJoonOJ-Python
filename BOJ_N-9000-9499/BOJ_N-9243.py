def main():
    N = int(input())
    A, B = list(input()), list(input())
    a, b = A[::], B[::]
    for _ in range(N):
        for ai in A:
            ai = '1' if a == '0' else '0'
    print("Deletion succeeded" if A == B else "Deletion failed")
    for _ in range(N):
        for i in range(len(a)):
            if a[i] == '0':
                a[i] = '1'
            else:
                a[i] = '0'
    print("Deletion succeeded" if a == b else "Deletion failed")


if __name__ == "__main__":
    main()
