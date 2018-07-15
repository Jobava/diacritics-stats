# wget https://dexonline.ro/static/download/scrabble/loc-flexiuni-5.0.zip
# unzip loc-flexiuni-5.0.zip
# cp loc-flexiuni-5.0.txt cu-diacritice

diacritics =     [c for c in "șțăîâ"]
non_diacritics = [c for c in "staia"]
index = lambda c, s: [i for i in range(len(s)) if s[i] == c][0]
strip_dia_char = lambda c: c if c not in diacritics else non_diacritics[index(c, diacritics)]
strip_dia = lambda word: "".join(strip_dia_char(c) for c in word)

homographs = {}
with open('cu-diacritice', 'r') as f:
    words = set([l.rstrip() for l in f])
    for word in words:
        dia_free_word = strip_dia(word)
        if dia_free_word in words:
            if dia_free_word in homographs:
                homographs[dia_free_word].append(word)
            else:
                homographs[dia_free_word] = [word]

homographs = {k:v for k,v in homographs.items() if len(homographs[k]) > 1}
len(homographs)
# 32859

len(set(w for v in homographs.values() for w in v))
# 67244

# 679683 cuvinte cu toate flexiunile.
# Din acestea avem 32859 de grupuri care scrise fără diacritice ar fi omografe.
# 67244 de cuvinte în total scrise fără diacritice sunt ambigue (aprox 10%).
