import hashlib


def main():
    S = input()
    encoded_S = S.encode()
    print(hashlib.sha256(encoded_S).hexdigest())


if __name__ == "__main__":
    main()
