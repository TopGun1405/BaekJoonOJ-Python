def main():
    N, U, L = map(int, input().split())
    print("Very Good" if N >= 1_000 and (U >= 8_000 or L >= 260)
          else ("Good" if N >= 1_000 else "Bad"))


if __name__ == "__main__":
    main()
