def main():
    N = int(input())
    for _ in range(N):
        ID = list(input())
        n1, n2 = sum(map(int, ID)), int(''.join(ID[-3:])) * 10
        Key = n1 + n2
        print(str(Key)[-4:] if Key >= 1000 else Key + 1000)


if __name__ == "__main__":
    main()
