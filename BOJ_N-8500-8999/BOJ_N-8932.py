def main():
    T = int(input())
    for _ in range(T):
        A, B, C, D, E, F, G = map(int, input().split())
        A = int(9.23076 * pow((26.7 - A), 1.835))
        B = int(1.84523 * pow((B - 75), 1.348))
        C = int(56.0211 * pow((C - 1.5), 1.05))
        D = int(4.99087 * pow((42.5 - D), 1.81))
        E = int(0.188807 * pow((E - 210), 1.41))
        F = int(15.9803 * pow((F - 3.8), 1.04))
        G = int(0.11193 * pow((254 - G), 1.88))
        print(A + B + C + D + E + F + G)


if __name__ == "__main__":
    main()
