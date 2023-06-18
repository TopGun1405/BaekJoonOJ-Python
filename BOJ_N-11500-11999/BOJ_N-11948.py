def main():
    sub = [int(input()) for _ in range(6)]
    sub.remove(min(sub[0:4]))
    print(sum(sub[0:3]) + max(sub[-2:]))


if __name__ == "__main__":
    main()
