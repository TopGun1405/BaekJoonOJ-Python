def main():
    N = int(input())
    for _ in range(N):
        name = input().split()
        name[0] = "god"
        print(''.join(name))


if __name__ == "__main__":
    main()
