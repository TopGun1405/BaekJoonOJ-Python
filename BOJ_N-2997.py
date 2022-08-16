def main():
    num = sorted(map(int, input().split()))
    print(2 * num[2] - num[1] if num[2] - num[1] == num[1] - num[0]
          else (num[2] - (num[2] - num[1]) // 2 if num[2] - num[1] > num[1] - num[0]
                else num[1] - (num[1] - num[0]) // 2))


if __name__ == "__main__":
    main()
