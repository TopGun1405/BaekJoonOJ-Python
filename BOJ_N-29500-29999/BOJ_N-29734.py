def main():
    N, M = map(int, input().split())
    T, S = map(int, input().split())

    Z = ((N // 8) * 8) + ((N // 8) * S) + (N % 8 if N % 8 else -S)
    D = T + ((M // 8) * 8) + ((M // 8) * (S + (T * 2))) + (M % 8 if M % 8 else -(S + (T * 2)))

    if Z < D:
        print("Zip")
        print(Z)
    else:
        print("Dok")
        print(D)


if __name__ == "__main__":
    main()
