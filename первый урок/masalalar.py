
print("=== Masala 1: Kalkulyator ===")

birinchi_son = float(input("Birinchi son: "))
amal = input("Amal (+, -, *, /): ")
ikkinchi_son = float(input("Ikkinchi son: "))

if amal == "+":
    natija = birinchi_son + ikkinchi_son
    print("Natija:", natija)
elif amal == "-":
    natija = birinchi_son - ikkinchi_son
    print("Natija:", natija)
elif amal == "*":
    natija = birinchi_son * ikkinchi_son
    print("Natija:", natija)
elif amal == "/":
    if ikkinchi_son == 0:
        print("Xato: Nolga bo'lib bo'lmaydi!")
    else:
        natija = birinchi_son / ikkinchi_son
        print("Natija:", natija)
else:
    print("Noto'g'ri amal belgisi!")



print("\n=== Masala 2: Chegirma hisoblash ===")

summa = float(input("Xarid summasi: "))

if summa > 500000:
    chegirma = 10
    tolov = summa - summa * 10 / 100
elif summa > 200000:
    chegirma = 5
    tolov = summa - summa * 5 / 100
else:
    chegirma = 0
    tolov = summa

if chegirma == 0:
    print("Chegirma yo'q")
else:
    print("Chegirma:", str(chegirma) + "%")

print("To'lov:", format(tolov, ",.0f"), "so'm")



print("\n=== Masala 3: Yosh toifasi ===")

yosh = int(input("Yoshingiz: "))

if yosh < 0:
    print("Xato: Yosh manfiy bo'lishi mumkin emas!")
elif yosh <= 12:
    print("Bola")
elif yosh <= 17:
    print("O'smir")
elif yosh <= 59:
    print("Kattalar")
else:
    print("Keksa")



print("\n=== Masala 4: Svetofor ===")

rang = input("Svetofor rangi: ").lower()

if rang == "qizil":
    print("To'xtang")
elif rang == "sariq":
    print("Tayyor turing")
elif rang == "yashil":
    print("Yuring")
else:
    print("Noma'lum rang")



print("\n=== Masala 5: Kun vaqtiga qarab salom ===")

soat = int(input("Soat (0-23): "))

if 5 <= soat <= 11:
    print("Xayrli tong")
elif 12 <= soat <= 17:
    print("Xayrli kun")
elif 18 <= soat <= 22:
    print("Xayrli kech")
else:
    print("Xayrli tun")
