def main():
    shortForm = {"CU": "see you",
                 ":-)": "I’m happy",
                 ":-(": "I’m unhappy",
                 ";-)": "wink",
                 ":-p": "stick out my tongue",
                 "(~.~)": "sleepy",
                 "TA": "totally awesome",
                 "CCC": "Canadian Computing Competition",
                 "CUZ": "because",
                 "TY": "thank-you",
                 "YW": "you’re welcome",
                 "TTYL": "talk to you later"}
    while True:
        p = input()
        print(shortForm[p] if p in shortForm else p)
        if p == "TTYL":
            break


if __name__ == "__main__":
    main()
