def main():
    N, M = map(int, input().split())
    name = [input() for _ in range(N)]
    pokedex = {name[i]: str(i + 1) for i in range(N)}
    pokedex2 = dict(map(reversed, pokedex.items()))
    prob = [input() for _ in range(M)]

    for i in range(M):
        if prob[i] in pokedex:
            print(pokedex[prob[i]])
        elif prob[i] in pokedex2:
            print(pokedex2[prob[i]])


if __name__ == "__main__":
    main()
