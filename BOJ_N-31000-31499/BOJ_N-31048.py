def main():
    facto = [1]
    for i in range(2, 11):
        facto.append(facto[-1] * i)

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(facto[N-1] % 10)


if __name__ == "__main__":
    main()
