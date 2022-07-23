yas = int(input("Yaşınızı Girin: "))
print("-"*15)

ilSaniye = 365*24*60*60

def hesap(yas, ilSaniye):
    yasSaniye = yas * ilSaniye
    return (yasSaniye)
cikti = hesap(yas, ilSaniye)
print("Yaşınızın Saniyə Qarşılığı: ", cikti)
