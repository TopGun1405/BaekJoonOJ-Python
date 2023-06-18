def main():
    w, l, h = int(input()), int(input()), int(input())
    print("good" if min(w, l) / h >= 2 and max(w, l) / min(w, l) <= 2 else "bad")


if __name__ == "__main__":
    main()