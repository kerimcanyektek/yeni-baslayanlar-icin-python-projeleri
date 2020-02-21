import random

n = 4
bulundu = 0
yerinde = 0
b = True
while b == True:
    r = random.randint(1000, 9999)
    rstr = str(r)
    b = False
    for i in range(0, n - 1):
        for j  in range(i + 1, n):
            if rstr[i] == rstr[j]: b = True

print("oyun başladı. uyuma...")

cikis = "0000"
tstr = ""
while tstr != cikis:
    b = True
    while b == True:
        tstr = input("tahmininiz giriniz. (0000-oyundan çıkar) :")
        if tstr == cikis:
            print("üzgünüm kaybettiniz...")
            print("tuttuğum sayı", rstr, "idi.")
            tstr = cikis
            break
        if tstr != cikis:
            b = False
            for i in range(0, n - 1):
                for j in range(i + 1, n):
                    if tstr[i] == tstr[j]: b = True
            if b == True:
                print("girilen sayının rakamları farklı olmalıdır...")

    if tstr != cikis:
        bulundu = 0; yerinde = 0
        for i in range(n):
            if rstr.find(tstr[i]) > -1: bulundu += 1
            if rstr[i] == tstr[i]: yerinde += 1
        print(bulundu, "tane bulundu...")
        print(yerinde, "tane yerinde...")
        
    if yerinde == n:
        print("tebrikler oyunu kazandınız...")
        tstr = cikis
