def main():
    text = input()
    alp = dict()
    for c in text:
        if c in alp:
            alp[c] += 1
        else:
            alp.update({c: 1})
    ans = "0/1"
    even = len(list(filter(lambda k: alp[k] % 2 == 0, alp)))
    odd = len(list(filter(lambda k: alp[k] % 2, alp)))
    if even > 0 and odd == 0:
        ans = '0'
    elif even == 0 and odd > 0:
        ans = '1'
    print(ans)


if __name__ == "__main__":
    main()
