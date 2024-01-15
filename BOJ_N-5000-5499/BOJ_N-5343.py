def main():
    n = int(input())
    for _ in range(n):
        data = input()
        error = 0
        for i in range(0, len(data), 8):
            oneBit = data[i:i+8][:-1].count("1")
            parityBit = data[i:i+8][-1]
            if oneBit % 2 == 1 and parityBit == "0":
                error += 1
            elif oneBit % 2 == 0 and parityBit == "1":
                error += 1
        print(error)


if __name__ == "__main__":
    main()
