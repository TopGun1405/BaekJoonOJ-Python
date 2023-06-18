def main():
    A, B = input().split()
    if len(A) > len(B):
        B = '0' * (len(A) - len(B)) + B
    elif len(B) > len(A):
        A = '0' * (len(B) - len(A)) + A
    C = ''
    for a, b in zip(A, B):
        C += str(int(a) + int(b))
    print(C)


if __name__ == "__main__":
    main()
