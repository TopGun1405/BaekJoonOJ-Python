def main():
    N = int(input())
    name = [input() for _ in range(N)]
    print("뭐야;" if 'anj' in name else "뭐야?")


if __name__ == "__main__":
    main()
