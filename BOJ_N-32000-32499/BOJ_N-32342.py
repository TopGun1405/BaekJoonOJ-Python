def main():
    Q = int(input())
    for _ in range(Q):
        S = input()
        wow = 0
        for i in range(len(S)-2):
            if S[i:i+3] == "WOW":
                wow += 1

        print(wow)


if __name__ == "__main__":
    main()
