def main():
    T1 = sorted(map(int, input().split()))
    T2 = sorted(map(int, input().split()))

    print("YES" if T1 == T2 and T1[2]**2 == T1[0]**2 + T1[1]**2 else "NO")


if __name__ == "__main__":
    main()
