def main():
    lights = list(input())

    cnt = 0
    for i, light in enumerate(lights):
        if lights == ["N"] * len(lights):
            break
        if light == "N":
            continue
        for n in range(i, len(lights), i+1):
            lights[n] = "N" if lights[n] == "Y" else "Y"
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
