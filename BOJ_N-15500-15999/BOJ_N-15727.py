def main():
    L = int(input())
    print(L // 5 if L % 5 == 0 else L // 5 + 1)


if __name__ == "__main__":
    main()
