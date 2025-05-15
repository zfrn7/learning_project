"""
for i in range(1, 6):
    print(f"{i} sayısının çarpım tablosu:")
    
    j = 1
  
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    
    print("-" * 20)
"""
def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for sayi in range(2, 101):
    if asal_mi(sayi):
        orijinal = sayi
        toplam = 0


        while sayi > 0:
            basamak = sayi % 10
            toplam += basamak
            sayi //= 10

        print(f"Asal sayı: {orijinal} | Basamak toplamı: {toplam}")
