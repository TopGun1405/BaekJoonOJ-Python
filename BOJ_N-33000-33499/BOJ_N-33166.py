def main():
    P, Q = map(int, input().split())
    A, B = map(int, input().split())
    print(P*A + (Q-P)*B if Q >= P else Q*A)


if __name__ == "__main__":
    main()
