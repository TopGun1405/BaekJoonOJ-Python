def main():
    while True:
        w = float(input())
        if w == -1:
            break
        print("Objects weighing {:0.2f} on Earth will weigh {:0.2f} on the moon.".format(w, w * 0.167))


if __name__ == "__main__":
    main()
