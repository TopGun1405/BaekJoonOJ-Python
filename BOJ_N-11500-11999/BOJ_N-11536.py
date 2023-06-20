def main():
    N = int(input())
    names = [input() for _ in range(N)]
    lines = sorted(names)
    print("INCREASING" if names == lines else ("DECREASING" if names == lines[::-1] else "NEITHER"))


if __name__ == "__main__":
    main()
