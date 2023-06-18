def main():
    N = int(input())
    for _ in range(N):
        txt = input()
        mid = len(txt) // 2
        if txt[mid - 1] == txt[mid]:
            print("Do-it")
        else:
            print("Do-it-Not")


if __name__ == "__main__":
    main()
