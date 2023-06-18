def main():
    T = int(input())
    for _ in range(T):
        w, u = input().split()
        if u == "kg":
            print("{:0.4f} lb".format(float(w) * 2.2046))
        elif u == "lb":
            print("{:0.4f} kg".format(float(w) * 0.4536))
        elif u == "l":
            print("{:0.4f} g".format(float(w) * 0.2642))
        elif u == "g":
            print("{:0.4f} l".format(float(w) * 3.7854))


if __name__ == "__main__":
    main()
