def main():
    K = int(input())
    if K == 1:
        print("AKARAKA")
    else:
        print("AKARAKA" + "RAKA" * (K-1))


if __name__ == "__main__":
    main()
