def main():
    candy = sorted(map(int, input().split()))
    print(2 * candy[2] - candy[1] - candy[0])


if __name__ == "__main__":
    main()
