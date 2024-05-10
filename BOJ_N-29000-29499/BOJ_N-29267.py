def main():
    n, k = map(int, input().split())
    ammo, a = 0, 0
    for _ in range(n):
        cmd = input()

        if cmd == "save":
            a = ammo
        elif cmd == "load":
            ammo = a
        elif cmd == "shoot":
            ammo -= 1
        elif cmd == "ammo":
            ammo += k

        print(ammo)


if __name__ == "__main__":
    main()
