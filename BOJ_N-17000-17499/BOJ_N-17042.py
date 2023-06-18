def main():
    elder = input()
    N = int(input())
    cntElder = {elder}
    for _ in range(N):
        Z1, Z2 = input().split()
        if Z2 == elder:
            elder = Z1
            cntElder.add(elder)
    print(elder)
    print(len(cntElder))


if __name__ == "__main__":
    main()
