def main():
    S_ab = int(input())
    M_a, F_ab, M_b = map(int, input().split())

    print("high speed rail" if (S_ab <= M_a + F_ab + M_b) or S_ab <= 240 else "flight")


if __name__ == "__main__":
    main()
