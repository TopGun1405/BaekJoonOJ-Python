def main():
    text = input()
    print("Canadian!" if text[-3:] == "eh?" else "Imposter!")


if __name__ == "__main__":
    main()
