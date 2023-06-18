def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        W = sum(map(int, input().split()))
        print("Equilibrium" if W == 0 else "Left" if W < 0 else "Right")


if __name__ == "__main__":
    main()
