def main():
    T = int(input())
    N = int(input())
    F = list(map(int, input().split()))
    print("Padaeng_i " + ("Happy" if sum(F) >= T else "Cry"))


if __name__ == "__main__":
    main()
