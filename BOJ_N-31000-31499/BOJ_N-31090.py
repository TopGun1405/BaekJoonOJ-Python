def main():
    T = int(input())
    for _ in range(T):
        N = input()
        print("Good" if (int(N) + 1) % int(N[-2:]) == 0 else "Bye")


if __name__ == "__main__":
    main()
