def main():
    typist = {"fdsajkl;": "in-out", "jkl;fdsa": "in-out",
              "asdf;lkj": "out-in", ";lkjasdf": "out-in",
              "asdfjkl;": "stairs",
              ";lkjfdsa": "reverse"}
    S = input()
    try:
        print(typist[S])
    except KeyError:
        print("molu")


if __name__ == "__main__":
    main()
