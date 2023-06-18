def main():
    d = int(input())
    for _ in range(d):
        p, q = map(int, input().split())
        print("f = {:.1f}".format(p * q / (p + q)))


if __name__ == "__main__":
    main()
