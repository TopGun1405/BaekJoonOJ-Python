def main():
    N = int(input())
    song = input()
    alp = {chr(n): 0 for n in range(97, 123)}
    for c in song:
        try:
            alp[c] += 1
        except KeyError:
            continue
    print(max(alp.values()))


if __name__ == "__main__":
    main()
