def main():
    T = int(input())
    for _ in range(T):

        n = int(input())
        chk = []
        for i in range(2, 65):

            num, k = [], n
            while k > 0:
                num.append(k % i)
                k //= i

            if num != num[::-1]:
                chk.append(0)

        print(0 if len(chk) == 63 else 1)


if __name__ == "__main__":
    main()
