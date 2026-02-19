def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        f = [float(input()) for _ in range(N)]

        avg = sum(f) / N
        error = list(filter(lambda e: abs(e - avg) >= 10.001, f))
    
        print(len(error))


if __name__ == "__main__":
    main()
