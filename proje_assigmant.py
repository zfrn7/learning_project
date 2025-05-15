isimler = ["Ali", "Ece", "Kaan", "Mete", "Batu", "Veli", "Ayşe"]
numaralar  = [145, 178, 164, 175, 185, 180, 134]

max_numara = 0
max_ogrenci = ""

for i in range(len(numaralar)):   # 0 1 2 3 4 5 6
    if numaralar[i] > max_numara:
        max_numara = numaralar[i]
        max_ogrenci = isimler[i]

print("En yüksek okul numarası: ", max_numara, " Sahibi olan öğrenci: ", max_ogrenci)
