def main():
    yName = input()
    N = int(input())
    teamName = {input(): 0 for _ in range(N)}

    LOVE = {'L': 0, 'O': 0, 'V': 0, 'E': 0}
    for c in yName:
        try:
            LOVE[c] += 1
        except KeyError:
            pass

    for name in teamName.keys():
        love = LOVE.copy()
        for c in name:
            try:
                love[c] += 1
            except KeyError:
                pass

        L, O, V, E = love.values()
        score = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
        teamName[name] = score

    print(sorted(teamName.items(), key=lambda k: (-k[1], k[0]))[0][0])


if __name__ == "__main__":
    main()
