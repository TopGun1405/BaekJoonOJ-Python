def main():
    n, c = map(int, input().split())

    a, bedroom, tot_area, balcony = 0, 0, 0, 0
    for _ in range(n):
        ai, ti = map(lambda e: int(e) if e.isdigit() else e, input().split())
        if ti != "balcony":
            tot_area += ai
            if ti == "bedroom":
                bedroom += ai
        else:
            balcony += ai
        a += ai

    print(a)
    print(bedroom)
    print((tot_area + (balcony / 2)) * c)


if __name__ == "__main__":
    main()
