ff = {
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    '2': 15,
    'joker': 16,
    'JOKER': 17,
}


def getCardType(t):
    if len(t) == 1:
        return 1, ff[t[0]]
    elif len(t) == 2:
        if t[0] == "joker" or t[0] == "JOKER":
            return 6, 20
        return 2, ff[t[0]]
    elif len(t) == 3:
        return 3, ff[t[0]]
    elif len(t) == 4:
        return 4, ff[t[0]]
    elif len(t) == 5:
        return 5, ff[t[0]]


while True:
    try:
        a, b = input().split('-')
        a = a.split()
        b = b.split()

        ty1, val1 = getCardType(a)
        ty2, val2 = getCardType(b)

        ttttt = None

        if ty1 == ty2 and ty1 in (1,2,3,4,5,6):
            if val1 > val2:
                ttttt = a
            elif val1 < val2:
                ttttt = b
            else:
                ttttt = ["ERROR"]
        elif ty1 == 6:
            ttttt = a
        elif ty2 == 6:
            ttttt = b
        elif ty1 == 4:
            ttttt = a
        elif ty2 == 4:
            ttttt = b
        else:
            ttttt = ["ERROR"]
        print(' '.join(ttttt))

    except:
        break
