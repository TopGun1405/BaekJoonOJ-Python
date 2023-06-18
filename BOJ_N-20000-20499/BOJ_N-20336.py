def main():
    n = int(input())
    menu = []
    for _ in range(n):
        setName = input().split()
        menu.append(setName)
    print(menu[0][0])
    print(*menu[0][1:], sep='\n')


if __name__ == "__main__":
    main()
