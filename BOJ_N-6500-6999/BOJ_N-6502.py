def main():
    cnt = 1
    while True:
        try:
            r, w, l = map(int, input().split())
        except ValueError:
            break
        d = (w / 2)**2 + (l / 2)**2
        print(f"Pizza {cnt} {'fits' if r**2 >= d else 'does not fit'} on the table.")
        cnt += 1


if __name__ == "__main__":
    main()
