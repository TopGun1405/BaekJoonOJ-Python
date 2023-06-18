def main():
    N = int(input())
    dancing = {"ChongChong"}
    for _ in range(N):
        Ai, Bi = input().split()
        if Ai in dancing:
            dancing.add(Bi)
        elif Bi in dancing:
            dancing.add(Ai)
    print(len(dancing))


if __name__ == "__main__":
    main()
