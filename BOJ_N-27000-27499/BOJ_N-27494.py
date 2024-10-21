def main():
    N = int(input())

    if N < 2023:
        print(0)
    else:
        cnt = 0
        for n in range(2023, N + 1):
            k = str(n)
            if not {"0", "2", "3"}.issubset(set(k)):
                continue

            num = []
            for c in k:
                if c == "2" and (len(num) == 0 or len(num) == 2):
                    num.append(c)
                elif c == "0" and len(num) == 1:
                    num.append(c)
                elif c == "3" and len(num) == 3:
                    cnt += 1
                    break

        print(cnt)
            

if __name__ == "__main__":
    main()
