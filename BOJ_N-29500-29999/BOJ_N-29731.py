def main():
    promise = [
        "Never gonna give you up",
        "Never gonna let you down",
        "Never gonna run around and desert you",
        "Never gonna make you cry",
        "Never gonna say goodbye",
        "Never gonna tell a lie and hurt you",
        "Never gonna stop"
    ]
    N = int(input())
    isChanged = False
    for _ in range(N):
        S = input()
        if S not in promise:
            isChanged = True
    print("Yes" if isChanged else "No")


if __name__ == "__main__":
    main()
