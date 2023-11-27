def main():
    n = int(input())
    fibo = [0, 1, 1, 1] + [0] * 113
    for i in range(4, 117):
        fibo[i] = fibo[i-2] + fibo[i-3] + fibo[i-4]
    print(fibo[n])


if __name__ == "__main__":
    main()
