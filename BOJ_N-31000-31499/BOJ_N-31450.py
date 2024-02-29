def main():
    M, K = map(int, input().split())
    print("Yes" if M % K == 0 else "No")


if __name__ == "__main__":
    main()
