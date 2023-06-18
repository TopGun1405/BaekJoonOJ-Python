def main():
    N = int(input())
    for _ in range(N):
        life = input().strip()
        score = 0
        for s in life:
            if s != ' ':
                score += ord(s) - 64
        print("PERFECT LIFE" if score == 100 else score)


if __name__ == "__main__":
    main()
