def main():
    S = input()
    Y, K = "YONSEI", "KOREA"
    for s in S:
        if not Y:
            print("YONSEI")
            break
        if not K:
            print("KOREA")
            break
        if s == Y[0]:
            Y = Y.replace(Y[0], '')
        if s == K[0]:
            K = K.replace(K[0], '')


if __name__ == "__main__":
    main()
