def main():
    while True:
        M, A, B = map(int, input().split())
        if M == A == B == 0:
            break
        t = round((M / A - M / B) * 3600)
        print("{}:{:02}:{:02}".format(t // 3600, t % 3600 // 60, t % 60))


if __name__ == "__main__":
    main()
