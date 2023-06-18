def main():
    w = sorted(map(int, input().split()))
    print(min(abs(w[3] - sum(w[:3])), abs((w[0] + w[3]) - (w[1] + w[2])), abs((w[0] + w[1]) - (w[2] + w[3]))))


if __name__ == "__main__":
    main()
