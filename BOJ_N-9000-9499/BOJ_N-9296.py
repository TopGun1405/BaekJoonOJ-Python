def main():
    T = int(input())
    for x in range(1, T + 1):
        L = int(input())
        ans = input()
        res = input()

        cnt = 0
        for ac, rc in zip(ans, res):
            if ac != rc:
                cnt += 1
        print(f"Case {x}: {cnt}")


if __name__ == "__main__":
    main()
