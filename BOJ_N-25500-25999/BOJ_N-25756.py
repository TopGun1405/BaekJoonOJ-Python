def main():
    N = int(input())
    Dura_neg = list(map(int, input().split()))
    curr_DN = Dura_neg[0]
    print(curr_DN)
    for i in range(1, N):
        curr_DN = (1 - (1 - curr_DN / 100) * (1 - Dura_neg[i] / 100)) * 100
        print("{:0.6f}".format(curr_DN))


if __name__ == "__main__":
    main()
