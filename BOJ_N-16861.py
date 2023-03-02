def main():
    n = input().strip()
    for num in range(int(''.join(n)), 1_000_000_001):
        if num % sum(map(int, list(str(num)))) == 0:
            print(num)
            break


if __name__ == "__main__":
    main()
