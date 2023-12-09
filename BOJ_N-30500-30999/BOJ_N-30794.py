def main():
    scores = {
        'miss': 0,
        'bad': 200,
        'cool': 400,
        'great': 600,
        'perfect': 1000
    }

    lv, detect = map(lambda e: int(e) if e.isdigit() else e, input().split())
    print(lv * scores[detect])


if __name__ == "__main__":
    main()
