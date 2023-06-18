def main():
    T = int(input())
    for _ in range(T):
        M, C = input().split()
        data = list(input().split())
        if C == 'C':
            for i in range(len(data)):
                data[i] = ord(data[i]) - 64
        else:
            for i in range(len(data)):
                data[i] = chr(int(data[i]) + 64)
        for i in range(len(data)):
            print(data[i], end=' ')
        print()


if __name__ == "__main__":
    main()
