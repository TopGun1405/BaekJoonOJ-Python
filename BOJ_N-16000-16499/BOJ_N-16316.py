def main():
    n = int(input())
    s = list(map(lambda e: int(e) if e != "mumble" else -1, input().split()))
    for i in range(n):
        if s[i] != -1 and s[i] != i + 1:
            print("something is fishy")
            break
    else:
        print("makes sense")


if __name__ == "__main__":
    main()
