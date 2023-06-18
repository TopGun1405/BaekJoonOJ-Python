def main():
    L = int(input())
    S = input()
    hashing = 0
    for i in range(len(S)):
        hashing += (ord(S[i]) - 96) * 31 ** i
    print(hashing % 1234567891 if hashing > 1234567891 else hashing)


if __name__ == "__main__":
    main()
