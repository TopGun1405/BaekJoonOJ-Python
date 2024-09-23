def main():
    N = int(input())
    if -2**15 <= N < 2**15:
        print("short")
    elif -2**31 <= N < 2**31:
        print("int")
    elif -2**63 <= N < 2**63:
        print("long long")


if __name__ == "__main__":
    main()
