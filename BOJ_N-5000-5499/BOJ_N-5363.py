def main():
    N = int(input())
    for _ in range(N):
        text = input().split()
        print(' '.join(text[2:] + text[:2]))


if __name__ == "__main__":
    main()
