def main():
    H, M, S = map(int, input().split())
    if S + 1 == 60 and M + 1 == 60:
        H = 0 if H + 1 == 24 else H + 1
    if S + 1 == 60:
        M = 0 if M + 1 == 60 else M + 1
    S = 0 if S + 1 == 60 else S + 1
    print("{:02d}:{:02d}:{:02d}".format(H, M, S))


if __name__ == "__main__":
    main()
