def main():
    N, A = input(), list(map(int, input().split()))
    M, B = input(), list(map(int, input().split()))
    score = 0
    for a in A:
        score = 0 if score + a in B else score + a
    print(score)


if __name__ == "__main__":
    main()
