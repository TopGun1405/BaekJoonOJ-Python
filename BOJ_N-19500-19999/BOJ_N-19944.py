def main():
    N, M = map(int, input().split())
    print("NEWBIE!" if M == 1 or M == 2 else ("OLDBIE!" if M <= N else "TLE!"))


if __name__ == "__main__":
    main()
