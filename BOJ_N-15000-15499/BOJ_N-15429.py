def main():
    n = int(input())
    for _ in range(n):
        gnome = list(map(int, input().split()))
        g, gnome = gnome[0], gnome[1:]

        for g_a, g_b in zip(gnome[:-1], gnome[1:]):
            if g_b <= g_a or g_b - g_a > 1:
                print(gnome.index(g_b) + 1)
                break


if __name__ == "__main__":
    main()
