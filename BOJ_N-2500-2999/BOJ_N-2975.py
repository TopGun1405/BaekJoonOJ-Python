def main():
    while True:
        A, op, B = input().split()
        if A == B == '0':
            break
        k = int(A) - int(B) if op == 'W' else int(A) + int(B)
        print("Not allowed" if k < -200 else k)


if __name__ == "__main__":
    main()
