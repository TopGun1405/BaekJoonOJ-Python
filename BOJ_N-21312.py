def main():
    A, B, C = map(int, input().split())
    cocktail = sorted([A, B, C, A*B, B*C, C*A, A*B*C], reverse=True)
    for taste in cocktail:
        if taste % 2:
            print(taste)
            break
    else:
        print(cocktail[0])


if __name__ == "__main__":
    main()
