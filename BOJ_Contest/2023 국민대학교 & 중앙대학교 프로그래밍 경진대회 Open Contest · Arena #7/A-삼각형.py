def main() -> None:
    W, H = map(int, input().split())
    print("{:0.1f}".format(W * H * 0.5))


if __name__ == "__main__":
    main()
