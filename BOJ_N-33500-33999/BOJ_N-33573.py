def main():
    T = int(input())
    for _ in range(T):
        N = input()

        A = int(N[::-1]) ** 0.5
        if int(A) == A and int(int(N) ** 0.5) == int(N) ** 0.5:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
