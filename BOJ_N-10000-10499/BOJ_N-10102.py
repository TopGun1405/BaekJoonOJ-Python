def main():
    V = int(input())
    vote = input()
    a = vote.count('A')
    b = V - a
    print('A' if a > b else ('B' if b > a else "Tie"))


if __name__ == "__main__":
    main()
