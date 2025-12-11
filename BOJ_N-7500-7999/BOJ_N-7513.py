def main():
    t = int(input())
    for i in range(1, t+1):
        m = int(input())
        words = [input() for _ in range(m)]

        print(f"Scenario #{i}:")
        n = int(input())
        for _ in range(n):
            info = list(map(int, input().split()))
            k, idx = info[0], info[1:]

            pw = [words[idx[j]] for j in range(k)]

            print("".join(pw))
        print()


if __name__ == "__main__":
    main()
