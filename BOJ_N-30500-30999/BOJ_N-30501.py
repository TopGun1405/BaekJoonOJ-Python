def main():
    N = int(input())
    criminal = ''
    for _ in range(N):
        name = input()
        if not criminal:
            if 'S' in name:
                criminal = name
    print(criminal)


if __name__ == "__main__":
    main()
