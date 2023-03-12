def main():
    N = int(input())
    S = input()
    print(["No", "Yes"][S[:N//2] == S[N//2:]])


if __name__ == "__main__":
    main()
