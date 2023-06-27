def main():
    C = int(input())
    for _ in range(C):
        N = list(map(int, input().split()))
        avg = sum(N[1:]) / N[0]
        up_avg = [n for n in N[1:] if n > avg]
        print("{:.3f}%".format(len(up_avg) / N[0] * 100))


if __name__ == "__main__":
    main()
