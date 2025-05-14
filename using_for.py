# for sayi in range(5):
#    print(sayi)
"""
meyveler = ("elma","armut","muz","kiraz")
for meyve in meyveler:
    print("en sevdiğim meyve", meyve)
    """
# for sayi in range(0,17,2):
 #   print(sayi)
""" for sayi in range(0,101,1):
    toplam += sayi
int(print(toplam))
toplam = 0 
for sayi in range(0, 101, 1):
    toplam += sayi
print(toplam)
 """
sayi1 = int(input("Lütfen bir sayı giriniz: "))
sayi2 = int(input("Lütfen bir sayı giriniz: "))

toplam = 0  

for sayi in range(sayi1, sayi2):
    if sayi % 2 != 0:
        print(sayi) 
        toplam += sayi

print("Toplam:", toplam)


