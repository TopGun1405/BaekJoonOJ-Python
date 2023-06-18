def main():
    t = sorted(map(int, input().split()))
    print(t[0] + t[1] + min(t[2], t[0] + t[1] - 1))


if __name__ == "__main__":
    main()
