def main():
    N, M = map(int, input().split())
    song = {}
    for _ in range(N):
        info = input().split()
        T, S, a = int(info[0]), info[1], info[2:5]
        try:
            song["".join(a)].append(S)
        except KeyError:
            song["".join(a)] = [S]

    for _ in range(M):
        b = "".join(input().split())
        if song.get(b, 0):
            print(song[b][0] if len(song[b]) == 1 else "?")
        else:
            print("!")


if __name__ == "__main__":
    main()
 