def main():
    T = int(input())
    for _ in range(T):
        M, N = input().split()

        if M == "1":
            res = ""
            IP = list(map(int, N.split(".")))
            for n in IP:
                res += bin(n)[2:].zfill(8)

            print(int(res, 2))

        else:
            res = ""
            IP = str(bin(int(N))[2:]).zfill(64)
            for i in range(8):
                res += str(int(IP[i*8:(i+1)*8], 2))
                if i != 7:
                    res += "."

            print(res)


if __name__ == "__main__":
    main()
