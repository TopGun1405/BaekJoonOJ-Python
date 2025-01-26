def main():
    D, A, K = map(int, input().split())
    # D = (a * A) + (k * K)

    for a in range(1, D//A+1):
        for k in range(1, D//K+1):
            if a*A + k*K == D:
                print(1)
                break
        else:
            continue
        break
    else:
        print(0)


if __name__ == "__main__":
    main()
