"""
meyveler = ["elma", "muz", "çilek", "portakal"]

aranan = input("Bir meyve adı girin: ")

if aranan in meyveler:
    print(f"{aranan} listede var.")
elif aranan == "":
    print("Boş giriş yaptınız.")
else:
    print(f"{aranan} listede yok.")
"""
"""
urunler = [
    {"isim": "laptop", "stok": 5},
    {"isim": "telefon", "stok": 0},
    {"isim": "kulaklık", "stok": 12},
    {"isim": "tablet", "stok": 2}
]

kullanici_urunu = input("Lütfen almak istediğiniz ürünü yazın: ").lower()

urun_bulundu = False

for urun in urunler:
    if urun["isim"] == kullanici_urunu:
        urun_bulundu = True
        if urun["stok"] > 5:
            print(f"{urun['isim']} stokta bol miktarda var ({urun['stok']} adet).")
        elif 1 <= urun["stok"] <= 5:
            print(f"{urun['isim']} stokta az kaldı ({urun['stok']} adet).")
        else:
            print(f"Üzgünüz, {urun['isim']} şu anda stokta yok.")
        break

if not urun_bulundu:
    print("Girdiğiniz ürün bulunamadı.")
"""
"""
# Değişkenler ve kullanıcı girdisi
isim = input("Adınızı girin: ")
vize = float(input("Vize notunuzu girin (0-100): "))
final = float(input("Final notunuzu girin (0-100): "))

# Aritmetik işlem (ortalama hesaplama)
ortalama = (vize * 0.4) + (final * 0.6)

# Koşullu ifadelerle değerlendirme
print(f"\n{isim}, not ortalaman: {ortalama:.2f}")

if ortalama >= 90:
    print("Tebrikler, notunuz: AA")
elif ortalama >= 80:
    print("Notunuz: BA")
elif ortalama >= 70:
    print("Notunuz: BB")
elif ortalama >= 60:
    print("Notunuz: CB")
elif ortalama >= 50:
    print("Notunuz: CC (Geçtiniz)")
else:
    print("Maalesef kaldınız. Notunuz: FF")
"""
kareler = [x**2 for x in range(1, 11)]
print(kareler)
