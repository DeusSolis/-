from collections import defaultdict
with open("input.txt", encoding="utf-8", mode="r") as f:
    ww = f.readlines()
    a1 = defaultdict(int)
    res_dct = {ww[i]: ww[i + 1] for i in range(0, len(ww), 2)}
    for a, b in res_dct:
        print(a,b)
        a1[a] += b
    # votes = defaultdict(int)
    # for a, b in ww:
    #     print(a, b)