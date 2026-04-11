def main():
    N, M = map(int, input().split())

    if M <= 26:
        obs = chr(ord("A") + M - 1)
    else:
        M -= 27
        obs = chr(ord("a") + M // 26) + chr(ord("a") + M % 26)

    print(f"SN {N}{obs}")


if __name__ == "__main__":
    main()
