
def tckimlikno_dogrulama(s):
    n = 11
    d = {}

    for i in range(1, n + 1):
        d[i] = int(s[i - 1])

    teklertoplam  = 0
    ciftlertoplam = 0

    for i in range(1, n - 1):
        if i % 2 != 0:
            teklertoplam  += d[i]
        else:
            ciftlertoplam += d[i]

    toplam1 = 3 * teklertoplam + ciftlertoplam
    q1      = (10 - toplam1 % 10) % 10

    toplam2 = 3 * (ciftlertoplam + q1) + teklertoplam
    q2      = (10 - toplam2 % 10) % 10

    if q1 == d[10] and q2 == d[11]:
        return True
    else:
        return False

s = '10000000146'

sonuc = tckimlikno_dogrulama(s)
if sonuc == True:
    print(s + ' : TC Kimlik No GEÇERLİDİR.')
else:
    print(s + ' : TC Kimlik No GEÇERLİ DEĞİLDİR.')
