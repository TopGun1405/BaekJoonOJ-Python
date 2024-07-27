def main():
    gold = 1.61803399
    d = int(input())
    for _ in range(d):
        phi, r = map(float, input().split())
        print("golden" if -gold * 0.01 <= phi/r - gold <= gold * 0.01 else "not")


if __name__ == "__main__":
    main()
