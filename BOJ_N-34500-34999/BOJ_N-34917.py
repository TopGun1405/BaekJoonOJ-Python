def main():
    T = int(input())
    for _ in range(T):
        N = int(input())

        for i in range(N//2+1):
            if i == 0:
                print("#" + "." * (N-2) + "#")
            elif 0 < i < N//2:
                print("#" + "." * (i-1) + "#" + "." * (N-(i+1)*2) + "#" + "." * (i-1) + "#")
            else:
                print("#" + "." * (i-1) + "#" + "." * (i-1) + "#")

        for _ in range(N//2):
            print("#" + "." * (N-2) + "#")


if __name__ == "__main__":
    main()
