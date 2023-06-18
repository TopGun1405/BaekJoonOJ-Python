def main():
    N = int(input())
    for _ in range(N):
        b, p = map(float, input().split())
        BPM, ABPM = 60 * b / p, 60 / p
        print("{:0.4f} {:0.4f} {:0.4f}".format(BPM - ABPM, BPM, BPM + ABPM))


if __name__ == "__main__":
    main()
