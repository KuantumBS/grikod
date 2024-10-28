from __future__ import annotations

def ikili_2_gri_kod(i2grik: str) -> str:
    # Dizeyi tamsayıya dönüştür
    i2grikod = int(i2grik, 2)
    
    # Gri (Gray) kodunu uygula
    i2grikod ^= (i2grikod >> 1)
    
    # Sonucu ikili sayı sistemiyle döndür
    return bin(i2grikod)[2:]

# Kullanıcıdan ikili sayı girişi al
i2grik = input("Bir ikili sistem (0, 1; Örnek: 101) sayısı giriniz: ")
gri_kod = ikili_2_gri_kod(i2grik)

# Gri kod sonucunu yazdır
# print(f"Gri Kod sayısı: {gri_kod}")
print("Gri Kod sayısı:", gri_kod)
