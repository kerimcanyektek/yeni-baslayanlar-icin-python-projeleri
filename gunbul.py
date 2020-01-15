#KeroKOD Python Projeleri Part: 6 / www.kerokod.com 

aylar  = {1:31, 2:00, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
gunler = {1:"PAZARTESİ", 2:"SALI", 3:"ÇARŞAMBA", 4:"PERŞEMBE", 5:"CUMA", 6:"CUMARTESİ", 7:"PAZAR"}

def artikyil(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return True
    else:
        return False

gun = int(input("günü giriniz :"))
ay  = int(input("ayı  giriniz :"))
yil = int(input("yılı giriniz :"))

toplam = (yil - 1) * 365 + int((yil - 1) / 4) - int((yil - 1) / 100) + int((yil - 1) / 400)
if artikyil(yil) == True:
    aylar[2] = 29
else:
    aylar[2] = 28

for i in range(1, ay-1+1):
    toplam += aylar[i]

toplam += gun

k = toplam - int(toplam / 7) * 7

if k == 0: k = 7

print(gun,".",ay,".",yil," :", gunler[k])
