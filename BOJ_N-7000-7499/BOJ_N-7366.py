def main():
    n = int(input())
    for i in range(1, n+1):
        m = int(input())
        words = input().split()

        s = words.count("sheep")

        print(f"Case {i}: This list contains {s} sheep.")
        if i < n:
            print()


if __name__ == "__main__":
    main()
