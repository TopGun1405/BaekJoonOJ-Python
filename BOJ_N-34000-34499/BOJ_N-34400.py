def main():
    T = int(input())
    for _ in range(T):
        t = int(input())
        print("ONLINE" if 0 <= t % 25 < 17 else "OFFLINE")


if __name__ == "__main__":
    main()
